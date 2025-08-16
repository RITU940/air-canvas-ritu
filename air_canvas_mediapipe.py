import cv2
import numpy as np
import os
from datetime import datetime

import mediapipe as mp

cap = cv2.VideoCapture(0)
canvas = None
prev_point = None

# Drawing state
draw_on = True       # press 'd' to toggle
show_landmarks = False
pen_color = (255, 0, 0)  # Blue in BGR
thickness = 5

os.makedirs("shots", exist_ok=True)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6,
)

def put_help(img):
    txt = "d: draw toggle  h: landmarks  1/2/3: color  [ ]: thickness  c: clear  s: save  q: quit"
    cv2.putText(img, txt, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (50, 50, 50), 2, cv2.LINE_AA)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read camera.")
        break

    frame = cv2.flip(frame, 1)
    if canvas is None:
        canvas = np.zeros_like(frame)

    h, w, _ = frame.shape

    # Process hand landmarks
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    tip_point = None

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Index fingertip is landmark 8
            tip = hand_landmarks.landmark[8]
            tip_point = (int(tip.x * w), int(tip.y * h))

            if show_landmarks:
                mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    mp_styles.get_default_hand_landmarks_style(),
                    mp_styles.get_default_hand_connections_style(),
                )

    # Draw line from previous point to current tip if drawing is on
    if draw_on and tip_point is not None:
        if prev_point is not None:
            cv2.line(canvas, prev_point, tip_point, pen_color, thickness, cv2.LINE_AA)
        prev_point = tip_point
    else:
        prev_point = None

    output = cv2.addWeighted(frame, 1.0, canvas, 1.0, 0)
    put_help(output)

    cv2.imshow("Air Canvas (MediaPipe)", output)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('d'):
        draw_on = not draw_on
    elif key == ord('h'):
        show_landmarks = not show_landmarks
    elif key == ord('c'):
        canvas = np.zeros_like(frame)
    elif key == ord('s'):
        fname = datetime.now().strftime("shots/air_canvas_%Y%m%d_%H%M%S.png")
        cv2.imwrite(fname, canvas)
        print("Saved:", fname)
    elif key == ord('1'):
        pen_color = (255, 0, 0)  # Blue
    elif key == ord('2'):
        pen_color = (0, 255, 0)  # Green
    elif key == ord('3'):
        pen_color = (0, 0, 255)  # Red
    elif key == ord(']'):
        thickness = min(50, thickness + 1)
    elif key == ord('['):
        thickness = max(1, thickness - 1)

cap.release()
hands.close()
cv2.destroyAllWindows()

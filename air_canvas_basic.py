import cv2
import numpy as np
import os
from datetime import datetime

cap = cv2.VideoCapture(0)
canvas = None
prev_point = None

# TODO: Replace these with values from color_tuner.py output
# Example for BLUE-ish color:
lower_hsv = np.array([100, 150, 50])
upper_hsv = np.array([140, 255, 255])

# Drawing state
pen_color = (255, 0, 0)  # Blue in BGR
thickness = 5

os.makedirs("shots", exist_ok=True)

kernel = np.ones((5, 5), np.uint8)

def put_help(img):
    txt = "1/2/3: color  [ ]: thickness  c: clear  s: save  q: quit"
    cv2.putText(img, txt, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (50, 50, 50), 2, cv2.LINE_AA)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read camera.")
        break

    frame = cv2.flip(frame, 1)
    if canvas is None:
        canvas = np.zeros_like(frame)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=1)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None

    if contours:
        c = max(contours, key=cv2.contourArea)
        if cv2.contourArea(c) > 800:
            M = cv2.moments(c)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                center = (cx, cy)

    # Draw line from previous center to current center
    if center is not None:
        if prev_point is not None:
            cv2.line(canvas, prev_point, center, pen_color, thickness, cv2.LINE_AA)
        prev_point = center
    else:
        prev_point = None

    # Overlay canvas on the frame
    output = cv2.addWeighted(frame, 1.0, canvas, 1.0, 0)

    # Small UI
    put_help(output)

    cv2.imshow("Air Canvas (Basic)", output)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
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
cv2.destroyAllWindows()

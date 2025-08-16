import cv2, mediapipe as mp
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils
while True:
    ok, img = cap.read()
    if not ok: break
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks:
        for h in res.multi_hand_landmarks:
            draw.draw_landmarks(img, h, mp.solutions.hands.HAND_CONNECTIONS)
    cv2.imshow("Hand Test", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release(); cv2.destroyAllWindows()
import cv2, mediapipe as mp
cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils
while True:
    ok, img = cap.read()
    if not ok: break
    res = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    if res.multi_hand_landmarks:
        for h in res.multi_hand_landmarks:
            draw.draw_landmarks(img, h, mp.solutions.hands.HAND_CONNECTIONS)
    cv2.imshow("Hand Test", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break
cap.release(); cv2.destroyAllWindows()


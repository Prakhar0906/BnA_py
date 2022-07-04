import cv2
import time
import hand_tracking_module as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)
detector = htm.handDetector()
while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw= False)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70),
                cv2.FONT_HERSHEY_COMPLEX, 2, (255, 8, 255), 2)

    cv2.imshow('hand', img)
    cv2.waitKey(1)

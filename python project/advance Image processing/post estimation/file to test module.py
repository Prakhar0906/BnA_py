import cv2
import mediapipe as mp
import time
import pose_module as pm
cap= cv2.VideoCapture('post estimation/videos/resized.mp4')
ptime= 0
detector= pm.poseDetector()
while True:
    success, img= cap.read()
    img= detector.findpose(img)
    lmList= detector.getPosition(img, draw= False)
    print(lmList[14])
    cv2.circle(img, (lmList[14][1], lmList[14][2]), 5, (255,8,233), cv2.FILLED)
    ctime= time.time()
    fps= 1/(ctime-ptime)
    ptime= ctime

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (233, 9, 233), 3)

    cv2.imshow('image', img)
    cv2.waitKey(1)
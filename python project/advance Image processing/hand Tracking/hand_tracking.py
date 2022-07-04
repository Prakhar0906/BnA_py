import cv2
import mediapipe as mp
import time 

cap= cv2.VideoCapture(0)
mpHands= mp.solutions.hands
hands= mpHands.Hands()

mpDraw= mp.solutions.drawing_utils

pTime= 0
cTime=0

while True:
    success, img=  cap.read()
    imageRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result= hands.process(imageRGB)
    #print(result.multi_hand_landmarks)
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                pass 

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cTime= time.time()
    fps= 1/(cTime-pTime)
    pTime= cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX,2 , (255,8,255), 2 )

    cv2.imshow('hand', img)
    cv2.waitKey(1)
    
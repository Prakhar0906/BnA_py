import cv2
import mediapipe as mp
import time

mpDraw= mp.solutions.drawing_utils

mpPose= mp.solutions.pose 
pose= mpPose.Pose()

cap= cv2.VideoCapture('post estimation/videos/resized.mp4')
ptime= 0
while True:
    success, img= cap.read()
    imageRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result= pose.process(imageRGB)
    #print(result.pose_landmarks)
    if result.pose_landmarks:
        mpDraw.draw_landmarks(img, result.pose_landmarks, mpPose.POSE_CONNECTIONS)

        for id, lm in enumerate(result.pose_landmarks.landmark):
            h,w,c= img.shape 
            cx, cy= int(lm.x*w), int(lm.y*h)
            cv2.circle(img, (cx, cy), 5, (255,8,233), cv2.FILLED)


    ctime= time.time()
    fps= 1/(ctime-ptime)
    ptime= ctime

    cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (233, 9, 233), 3)

    cv2.imshow('image', img)
    cv2.waitKey(1)

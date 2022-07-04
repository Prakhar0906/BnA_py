import cv2
import mediapipe as mp
import time 

cap= cv2.VideoCapture(0)#('post estimation/videos/resized.mp4')
pTime=0

mpFaceDetection= mp.solutions.face_detection
mpDraw= mp.solutions.drawing_utils
faceDetection= mpFaceDetection.FaceDetection(0.75)

while True:
    success, img= cap.read()

    imageRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result= faceDetection.process(imageRGB)
    
    if result.detections:
        for id, detection in enumerate(result.detections): 
            #mpDraw.draw_detection(img, detection)
            #print(id, detection)
            #print(detection.score)
            bboxC= detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox= int(bboxC.xmin * iw), int(bboxC.ymin * ih),\
                int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(img, bbox, (0,255,0), 2)
            cv2.putText(img, f'Con: {int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)


    cTime= time.time()
    fps= 1/(cTime-pTime)
    pTime= cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 2, (0,255,0), 2)
    cv2.imshow('video', img)
    cv2.waitKey(1)

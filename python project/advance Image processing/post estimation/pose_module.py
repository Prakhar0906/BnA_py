import cv2
import mediapipe as mp
import time




class poseDetector:
    def __init__(self, mode= False, upBody= False, smooth= True, detectionCon= 0.5, trackingCon= 0.5):
        self.mode= mode
        self.upBody= upBody
        self.smooth= smooth
        self.detectionCon= detectionCon
        self.trackingCon= trackingCon 

        self.mpDraw= mp.solutions.drawing_utils
        self.mpPose= mp.solutions.pose 
        self.pose= self.mpPose.Pose(self.mode, self.upBody, self.smooth, self.detectionCon, self.trackingCon)

    def findpose(self, img, draw= True):

        imageRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result= self.pose.process(imageRGB)
        #print(result.pose_landmarks)
        if self.result.pose_landmarks:
             if draw:
                self.mpDraw.draw_landmarks(img, self.result.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def getPosition(self, img, draw= True):
        lmList= []
        if self.result.pose_landmarks:
            for id, lm in enumerate(self.result.pose_landmarks.landmark):
                h,w,c= img.shape 
                cx, cy= int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255,8,233), cv2.FILLED)
        return lmList


    

def main():
    cap= cv2.VideoCapture('post estimation/videos/resized.mp4')
    ptime= 0
    detector= poseDetector()
    while True:
        success, img= cap.read()
        img= detector.findpose(img)
        lmList= detector.getPosition(img, draw= False)
        #print(lmList[10])
        #cv2.circle(img, (lmList[10][1], lmList[10][2]), 5, (255,8,233), cv2.FILLED)
        ctime= time.time()
        fps= 1/(ctime-ptime)
        ptime= ctime

        cv2.putText(img, str(int(fps)), (10, 50), cv2.FONT_HERSHEY_PLAIN, 3, (233, 9, 233), 3)

        cv2.imshow('image', img)
        cv2.waitKey(1)



if __name__ == "__main__":
    main()
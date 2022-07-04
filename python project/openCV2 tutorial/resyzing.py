import cv2 as cv



def rescaleFrame(frame, scale= 0.75):
    #image video live video 
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimentions= (width, height)

    return cv.resize(frame, dimentions, interpolation=cv.INTER_AREA)

def changeres(width, height):
    #live video 
    capture.set(3, width)
    capture.set(4, height)
    

capture = cv.VideoCapture(0)

while True:
    isTrue, frame= capture.read()
    frame_resized= rescaleFrame(frame)
    #cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()



cv.waitKey(0)
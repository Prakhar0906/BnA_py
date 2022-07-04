import cv2 as cv

#img= cv.imread('Saved Pictures/animals1.jpg')
#cv.imshow('panda', img)

#Grey scale
#grey= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Grey', grey)

capture= cv.VideoCapture(0)

while True:
    isTrue, frame= capture.read()
    grey= cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('grey', grey)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
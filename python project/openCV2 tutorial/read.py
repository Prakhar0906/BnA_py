import cv2 as cv

img= cv.imread('Saved Pictures/animals1.jpg')
cv.imshow('panda', img)

cv.waitKey(0)
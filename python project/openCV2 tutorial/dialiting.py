import cv2 as cv

img= cv.imread('Saved Pictures/animals1.jpg')

blur= cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

canny= cv.Canny(blur, 125, 175)

cv.imshow('canny', canny)

dilated= cv.dilate(canny, (3,3), iterations=1)

erode= cv.erode(dilated, (3,3), iterations=1)
cv.imshow('erode', erode)

cv.imshow('dialeted', dilated)

cv.waitKey(0)
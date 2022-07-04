import cv2 as cv

img= cv.imread('Saved Pictures/animals1.jpg')

blur= cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

canny= cv.Canny(blur, 125, 175)

cv.imshow('canny', canny)

cv.waitKey(0)
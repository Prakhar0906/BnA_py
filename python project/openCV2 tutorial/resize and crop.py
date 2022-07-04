import cv2 as cv 

img= cv.imread('Saved Pictures/animals1.jpg')

#resizing 

resized= cv.resize(img, (400,300))
cv.imshow('resized', resized)

#cropping 
cropped= img[50:100, 50:100]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
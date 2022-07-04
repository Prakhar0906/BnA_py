import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')

blank[200:300, 300:400]= 0,0,255 #color a certain portion

cv.rectangle(blank, (0,0), (250,250), (255,0,0), thickness= 1)
#^ the image to show on, origin, end, color, thickness of line can be point Filled == 1

cv.circle(blank, (250,250), 40, (0,255,0), thickness= 2)
#^ the image to show on, origin, radius, color, thickness (-1) for filled

cv.line(blank, (30,30), (100, 100), (255,0,255), thickness=2)
#^ the image, start, end, color, thickness only

cv.putText( blank, 'hi', (100,300), cv.FONT_HERSHEY_COMPLEX, 1.0, (100,100,100))



cv.imshow('blank', blank)

cv.waitKey(0)
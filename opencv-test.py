import cv2 as cv
import numpy as np

#Image reading
#cv.imread('file directory', flag)
#flag=0: grayscale
#flag=1: colorscale
#flag=-1: image with alpha channel
img = cv.imread("Resources/SIUUU.jpg", 1)

#Printing image matrix
print(img)

#Show imagen on screen
cv.imshow('SIUUU', img)

#Stop window from closing instantly
#It receives time in milliseconds, but 0 means nevers closes until we click "close"
cv.waitKey(0)
#cv.destroyAllWindows()

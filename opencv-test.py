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
key_value = cv.waitKey(0)

#If Key Value is 27 means that ESC Key was press.
#Condition: if we press ESC it'll close all windows, but it we press 's' it'll make a copy of
#our image and then close all windows.
if key_value == 27:
    cv.destroyAllWindows()
elif key_value == ord('s'):
    cv.imwrite('Resources/SIUUU_COPY.png', img)
    cv.destroyAllWindows()


import cv2
import numpy as np
img = cv2.imread('colors.png',1)
px=img[100,100]
print(px)

#accessing only blue pixel 
blue=img[100,100,0]
print(blue)

#modification of pixel value
img[100,100] = [255,255,255]
print(img[100,100])

#show img
cv2.imshow('image_window_name',img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()

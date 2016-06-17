import numpy as np
import cv2
#for gray scale
img=cv2.imread('apple1.jpg',-1)

#show image 
cv2.namedWindow('image_window',cv2.WINDOW_NORMAL)
cv2.imshow('image_window',img)

#write
cv2.imwrite('applegrey.png',img)

k=cv2.waitKey(100000)#time in ms

cv2.destroyAllWindows()

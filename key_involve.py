import numpy as np
import cv2
#for gray scale
img=cv2.imread('/home/himanshu/Desktop/iisc/pictures/apple1.jpg',0)

#show image 
cv2.namedWindow('image_window',cv2.WINDOW_NORMAL)
cv2.imshow('image_window',img)

k=cv2.waitKey(0)

if k==ord(s):
	cv2.imwrite('applegrey.png',img)
	cv2.destroyAllWindows()

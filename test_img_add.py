import numpy as np
import cv2
img1=cv2.imread('/home/himanshu/Desktop/iisc/pictures/img1.png',1)
img2=cv2.imread('/home/himanshu/Desktop/iisc/pictures/img2.png',1)
res=img1+img2 #numpy add
cv2.imshow('image',res)

#write
cv2.imwrite('combined.png',res)
k=cv2.waitKey(0)
cv2.destroyAllWindows()

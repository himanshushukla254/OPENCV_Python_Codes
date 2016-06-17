import numpy as np
import cv2
img1=cv2.imread('img1.png',1)
img2=cv2.imread('img2.png',1)
res=cv2.addWeighted(img1,0.7,img2,0.3,0)
cv2.imshow('image',res)

#write
#cv2.imwrite('combined.png',res)
k=cv2.waitKey(0)
cv2.destroyAllWindows()

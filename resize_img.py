import cv2
import numpy as np
img= cv2.imread('apple1.jpg')
res=cv2.resize(img,None,fx=1,fy=2,interpolation=cv2.INTER_CUBIC)

#height, width = img.shape[:2]
#res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

cv2.imshow('img',img)
cv2.imshow('res_img',res)

k=cv2.waitKey(0)
cv2.destroyAllWindows()

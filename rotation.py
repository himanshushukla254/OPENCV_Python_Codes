import cv2
import numpy as np
img = cv2.imread('apple1.jpg',1)
rows=100
cols=100
M = cv2.getRotationMatrix2D((50,50),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img_window',img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2
#for gray scale
img=cv2.imread('apple1.jpg',-1)

#show image 
cv2.imshow('show_image',img)

#write
cv2.imwrite('applegrey.png',img)

k=cv2.waitKey(0)
cv2.destroyAllWindows()

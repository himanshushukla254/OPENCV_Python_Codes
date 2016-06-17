import numpy as np
import cv2
img=cv2.imread('/home/himanshu/Desktop/iisc/pictures/472.jpg',1)

area= img[280:340, 330:390]
#copying of area 
img[273:333, 100:160] = area

#splitting and merging 
#b,g,r = cv2.split(img)
#img = cv2.merge((b,g,r))

cv2.imshow('show_image',img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()

import numpy as np
import cv2
#black img
img=np.zeros((512,512,3),np.uint8)
#draw a diagonal line of thickness 5px
cv2.line(img,(0,0),(511,511),(255,0,0),5)
cv2.imshow('img',img)
#cv2.imwrite('line.png',img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()



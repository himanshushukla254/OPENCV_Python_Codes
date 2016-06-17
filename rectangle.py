import numpy as np
import cv2
#create a black img
img=np.zeros((512,512,3),np.uint8)

#draw a rectangle of thickness 5px on that img
#cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)


#draw circle
#cv2.circle(img,(447,63), 63, (0,0,255), -1)


#drawing ellipse
#cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

#text on img 
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_4)


#show img
cv2.imshow('img',img)

k=cv2.waitKey(0)
cv2.destroyAllWindows()



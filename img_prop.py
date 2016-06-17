import cv2
import numpy as np
img = cv2.imread('/home/himanshu/Desktop/iisc/pictures/colors.png',1)

print(img.shape)
print(img.size)
print(img.dtype)

#show img
cv2.imshow('image_window_name',img)
k=cv2.waitKey(0)
cv2.destroyAllWindows()

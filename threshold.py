# import opencv
import cv2
 
# Read image
src = cv2.imread("/home/himanshu/Desktop/iisc/pictures/threshold.png", cv2.IMREAD_GRAYSCALE)
 
# Set threshold and maxValue
thresh = 0
maxValue = 255
 
# Basic threshold example
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY);
cv2.imshow('image',dst)
k=cv2.waitKey(0)
cv2.destroyAllWindows()

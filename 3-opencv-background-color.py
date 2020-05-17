#import cv2 module 
import cv2

#read image 
img = cv2.imread('shirt.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)

cv2.waitKey(0)
cv2.destroyAllWindows()



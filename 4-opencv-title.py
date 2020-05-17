#import cv2 module 
import cv2

#read image 
img = cv2.imread('shirt.jpg',cv2.IMREAD_GRAYSCALE)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'hi',(10,20), font, .5,(255,255,255),2,cv2.LINE_AA) 
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

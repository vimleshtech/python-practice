#signup : https://developer.twitter.com/

import cv2

cv2.namedWindow("preview")  #assign title of frame
vc = cv2.VideoCapture(0)    #open the frame with gray     


if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()  #current frame reference 
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC        
        break

     
    
cv2.destroyWindow("preview")

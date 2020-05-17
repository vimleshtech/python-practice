import cv2
import numpy as np
img = np.zeros((500,500,3),dtype = 'uint8') # Create a dummy image

#press q to exit 
while True:
    cv2.imshow('a',img)
    k = cv2.waitKey(0)
    print(k)
    if k == ord('q'):
        break
cv2.destroyAllWindows()

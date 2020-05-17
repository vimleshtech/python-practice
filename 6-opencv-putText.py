import cv2
# Read the image
img = cv2.imread('img2.png')

# initialize counter
i = 0
while True:
    # Display the image
    cv2.imshow('a',img)
    
    # wait for keypress
    k = cv2.waitKey(0)
    
    # specify the font and draw the key using puttext
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(img,chr(k),(10+i,50), font, .5,(255,255,255),2,cv2.LINE_AA)
    
    i+=10


    if k == ord('q'):
        break
cv2.destroyAllWindows()

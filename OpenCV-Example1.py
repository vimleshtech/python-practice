import cv2
#img = cv2.imread('shirt.jpg')
img = cv2.imread('shirt.jpg',0)

print(img) #object of image in nd
print(img.shape)

#(179, 150, 3)
cv2.imshow('shirt',img)

cv2.waitKey(0)
 
cv2.destroyAllWindows()



'''
[
     [
     [ ]
     [ ]
     [ ]
     [ ]
     [ ]
     ]

     
     [
     [ ]
     [ ]
     [ ]
     [ ]
     [ ]
     ]
     [
     [ ]
     [ ]
     [ ]
     [ ]
     [ ]
     ]
]
'''






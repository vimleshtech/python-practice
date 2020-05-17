import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False


cv2.imshow("preview", frame)
rval, frame = vc.read()

cv2.imwrite('opencv.png', frame)

cv2.waitKey(0)
cv2.destroyWindow("preview")

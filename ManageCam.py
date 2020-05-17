from tkinter import *
import cv2


window = Tk()


lbl = Label(text='Enter profile name ')
lbl.pack()

txt = Entry()
txt.pack()

#add event on button click
def open_cam():
     
     
     cv2.namedWindow("preview")
     vc = cv2.VideoCapture(0)
     
     #print(vc)
     #print(vc.isOpened())
     if vc.isOpened():
          rval, frame = vc.read()
          #print(rval)
          #print(frame)
          
     else:
          vc = False

     pname = txt.get() #read from entry field
     src = r'C:\Users\vkumar15\Desktop\img'
     pname  = src+'\\'+pname
     
     cv2.imshow("preview", frame)
     rval, frame = vc.read()
     #print(rval)
     #print(frame)
     key = cv2.waitKey(0)
     print(key)
     if key == 65:
          cv2.imwrite(pname+'.png', frame)     
          cv2.destroyWindow("preview")

          



btn = Button(text='Open Cam',command=open_cam)
btn.pack()



window.mainloop()



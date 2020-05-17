
#GUI : graphical user interface
from tkinter import *
from MultipleRegressionExample import car_model
from sklearn.linear_model import LinearRegression

o = Tk()


#'cyl','disp','hp','drat','wt'
l1 = Label(text='enter cyl ')
l1.pack()

cyl = Entry()
cyl.pack()

l2 = Label(text='enter disp ')
l2.pack()

disp = Entry()
disp.pack()


l3 = Label(text='enter hp ')
l3.pack()

hp = Entry()
hp.pack()



l4 = Label(text='enter drat ')
l4.pack()

drat = Entry()
drat.pack()


l5 = Label(text='enter wt ')
l5.pack()

wt = Entry()
wt.pack()


msg = Label(text='')
msg.pack()

def predict():
    w  = float(wt.get())
    c   = float(cyl.get())
    h  = float(hp.get())
    da  = float(drat.get())
    di  = float(disp.get())

    lm = car_model()
    res = lm.predict([[c,di,h,da,w]])
    
    msg.configure(text=str(res[0][0]))
    
    
    #print('test call ')
    #print(res)
    


btn = Button(text='Predict',command=predict)
btn.pack()

o.mainloop()




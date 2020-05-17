import pandas as pd
from sklearn.linear_model import LinearRegression 

def car_model():
    path=r'C:\Users\vkumar15\Documents\Training\Training\Excel VBA\Excel\Car_dataset.xlsx'
    car = pd.read_excel (path,sheet_name='Sheet1')

    #print(car)
    #cor = car.corr()
    #print(cor)
    #cor.to_csv(r'C:\Users\vkumar15\Desktop\car_corr.csv')

    #x : independent variables 
    # cyl	disp	hp	drat	wt
    #y : dependent variable
    #mpg
    #split data
    x = car[['cyl','disp','hp','drat','wt']]
    y = car[['mpg']]
    #print(x)
    #print(y)

    #create object
    lm= LinearRegression()
    lm.fit(x,y) #learn from data
    return lm


##get coff, intercept
#print(lm.intercept_)
#print(lm.coef_)

























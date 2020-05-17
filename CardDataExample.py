import pandas as pd

import matplotlib.pyplot as plt 

#read csv file 
cars = pd.read_excel(r'C:\Users\vkumar15\Desktop\Learning & Training\Python-Batch-20thMay\data\Car_dataset.xlsx', sheet_name='Sheet1')

print(cars)
print(cars.shape)

print(cars.columns)

print(cars.info())

#show stats
print(cars.describe())


#Correlation: which attributes or features will impact to mpg
print(cars.corr())
#c =cars.corr()
#c.to_csv('corr_outptu.csv')


#show graph
#cars.plot() #default type is line chart
#plt.show()


#cars.plot(kind='bar') #default type is line chart
cars.plot(kind='box') #default type is line chart
plt.show()






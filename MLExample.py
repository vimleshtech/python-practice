import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r'C:\Users\vkumar15\Desktop\cardata.csv')
print(df)

#show size of table/shape
print(df.shape) # row,col

#show particular column
print(df['CAR_NAME'])

##
out = df.corr() #method='Pareson'
print(out)


##save corr output to file
#out.to_csv(r'C:\Users\vkumar15\Desktop\corr_output.csv')
#print('result saved '      )

#df.plot()
df.plot(kind='bar')
#plt.show()



##stats
print(df.info())
print(df.describe())





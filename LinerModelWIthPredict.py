import numpy as np
from sklearn.linear_model import LinearRegression

height =[140,155,156,134,143,149]
x = np.array(height).reshape((-1, 1))
print(x)


weight =[51,62,72,45,52,56]
y = np.array(weight)
print(y)

#
reg = LinearRegression()
reg.fit(x,y)

print(reg.intercept_)

#predict
h = int(input('enter height :'))

o = reg.predict([[h]])
print(o)



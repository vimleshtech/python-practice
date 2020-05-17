import numpy as np

a = [[1,2,3],[1,2,3],[1,2,3]]
b = [[10,12,30],[1,2,3],[11,12,13]]

x = np.array(a)
y = np.array(b)

print(x)
print(y)

#operation
print(np.add(x,y))
print(np.subtract(x,y))
print(np.divide(x,y))
print(np.multiply(x,y))

##read data by index
print(x[1]) #read 2nd row
print(x[1,2]) #read 2nd row and 3rd value

x = np.arange(1,11)
y = x*2
print(x)
print(y)








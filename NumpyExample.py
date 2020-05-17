import numpy as np

#create array of given range
n =np.arange(1,10)  
print(n)

#2nd exammple
n =np.arange(1,10,.2)  #.2 is incrementer 
print(n)

#Diff between list and array
l = [1,2,3,4,5] #list
a = np.arange(1,6) #array

print(type(l))
print(l)
print(type(a))
print(a)

##
print(l*2) #[1 ,2,3,4,5,1,2,3,4,5]
print(a*2) #[2,4,6,8,10]


#convert list to array
x =[111,22,333,444,55,666]
a = np.array(x)
print(a)

##show to shape
print(a.shape)

#reshape
a = np.array(x).reshape(-1,1) #-1 : by row , 1 is dimenssion
print(a)



#convert to 2 dimenssion
a = np.array(x).reshape(-1,2) #-1 : by row , 2 is dimenssion
print(a)

##data type / change or assign data type
a = np.array(x,dtype=float)
print(a)

#generate series of 0
x = np.zeros(10)
print(x)

#generate one series
x = np.ones(10)
print(x)




















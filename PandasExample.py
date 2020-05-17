import pandas as pd

#create empty dataframe(is table)
df = pd.DataFrame()
print(df)


#create dataframe from list and dict
emp = {'eid':[1,2,3,4,10,5],
       'name':['Nitin','Jatin','Divya','Ayush','Nitisha','Kshitiz'],
       'gender':['male','male','female','male','female','male'],
       'sal':[23000,56000,40000,34000,46000,120000]
       }

df = pd.DataFrame(data=emp)

print(df)
#show all columns
print(df.columns)

#print rows from top
print(df.head(2))

#print from buttom
print(df.tail(1))


#show selected column
print(df['name'])
print(df[['name','sal']])


#filter row
print( df[df['eid']==2] )

m =  df[df['gender']=='male'] 
f =  df[df['gender']=='female']

print('male')
print(m)
print('female')
print(f)


#sort data
print(df.sort_values('sal',ascending=True)) #in asc 
print(df.sort_values('sal',ascending=False)) #in desc

print(df.sort_values('name',ascending=False)) #in desc



#save data in csv file
df.to_csv('emp_data.csv')
print('data is saved')






      

















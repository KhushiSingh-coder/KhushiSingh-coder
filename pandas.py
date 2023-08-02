# Pandas

import pandas as pd
'''
● The primary two data structure of pandas are Series and Dataframe Series: 
● A one-dimensional labeled array capable of holding any data type.
● A Series is essentially a column.'''

s = pd.Series([3, -5, 2, 1], index=['a', 'b', 'c', 'd'])
print(s)

s = pd.Series(['Three', 'Five', 'Two', 1], index=['a', 'b', 'c', 'd'])
print(s)

# dataFrame
#● A two-dimensional labeled data structure with columns of potentially different types
# intialise data of lists.
data = {'Name': ['snehal', 'anusha', 'sheetal', 'rohit'], 'Age': [20, 21, 19, 18]}
# Create DataFrame
df = pd.DataFrame(data)
 # Print the output.
print(df)


'''Column selection:
● In Order to select a column in Pandas DataFrame, we can either access the columns 
by calling them by their columns name.
Example: print(df[['Age']])'''


print(df['Name'])


'''Column addition:
● We will understand this by adding a new column to an existing data frame.
 Example: '''
address = ['mumbai', 'Thane', 'kalyan', 'Mulund']
df['Address'] = address
print(df)


'''Column Deletion:
● Columns can be deleted or popped'''
df.drop(["Age"],axis = 1)
print(df)

df.drop(["Age"], axis=1, inplace=True)
print(df)


#Row selection:
#We can select rows using loc[] function
print(df.loc[2])

#We can select multiple rows using head()
print(df.head())
print(df.head(2))

print(df.tail())
print(df.tail(1))

'''
Row addition:
● We will understand this by adding a new row to an existing data frame using 
loc[],append() and concat().
 Example: 
 Using loc:'''
df.loc[1]=['sam','mumbai']
print(df)

#Using append():
print(df.append({'Name':'juhi','Age':22,'Address':'Nasik'}, ignore_index=True))


#Using concat():
new_row = pd.DataFrame({'Name':'abhishekh',
 'Age':24,
 'Address':'thane'},index=[4])
df1=pd.concat([new_row,df])
print(df1)

print(df1.sort_index())


#Row Deletion:
''' Rows can be deleted or popped
 Example: '''
df.drop([1],inplace = True)
print(df)
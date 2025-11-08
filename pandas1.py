import pandas as pd # Importing the pandas library for data manipulation and analysis
import numpy as np # Importing numpy for numerical operations

#checking pandas version
print(pd.__version__)

#Creating a Series
s1= pd.Series(['beetroot','carrot','tomato','kovakkai','coconut'])
print(s1)

#Creating a Series with custom index
s2= pd.Series(['beetroot','carrot','tomato','kovakkai','coconut'], index=[101,102,103,104,105])
print(s2)

#Creating a Series from a dictionary
s3= pd.Series({'a':10,'b':20,'c':30,'d':40})
print(s3)

#Accessing elements in a Series
print(s2[103]) #Accessing by index label
print(s2.iloc[2]) #Accessing by integer location
print(s3['c']) #Accessing by index label
print(s3.iloc[2]) #Accessing by integer location

#drop elements from a Series
s4= s2.drop(102)
print(s4)
print(s2) #original Series remains unchanged
s2.drop(104, inplace=True) #dropping in place
print(s2)

#Creating a DataFrame
data= {'vegetable': ['beetroot','carrot','tomato','kovakkai','coconut'],
       'color': ['red','orange','red','green','brown'],
       'unit': ['1kg','1kg','1kg','500g','1pc'],
       'min' : [15,25,53,30,'seventeen'],
         'max' : [40,45,90,45,38]}

maruthamunai_market= pd.DataFrame(data)#Creating DataFrame from dictionary
print(maruthamunai_market)


maruthamunai_market.index= ['a','b','c','d','e']#custom index
print(maruthamunai_market)

print('Accessing columns in DataFrame')
print(maruthamunai_market['vegetable']) #Accessing single column
print(maruthamunai_market[['vegetable','color']]) #Accessing multiple columns
print(maruthamunai_market.loc[:,'vegetable']) #Accessing single column using loc

#Accessing rows in DataFrame
print(maruthamunai_market.loc['c']) #Accessing by index label
print(maruthamunai_market.iloc[2]) #Accessing by integer location
print(maruthamunai_market.loc['b':'d']) #Accessing range of rows by index label
print(maruthamunai_market.iloc[1:4]) #Accessing range of rows by integer location

#Accessing specific elements
print(maruthamunai_market.at['c','color']) #Accessing by index label
print(maruthamunai_market.iat[2,1]) #Accessing by integer location

#Adding a new column
maruthamunai_market['price_per_unit'] = [30, 20, 50, 15, 25]
print(maruthamunai_market)

#Removing a column
mar = maruthamunai_market.drop('price_per_unit', axis=1,) #Removing 'price_per_unit' column (not in place)
print(mar)
print(maruthamunai_market) #original DataFrame remains unchanged
maruthamunai_market.drop('unit', axis=1, inplace=True)#Removing 'unit' column in place
print(maruthamunai_market)

print(maruthamunai_market.isna().sum())#check for missing values

maruthamunai_market['season']= ['True','True','False','True',np.nan]#adding new column with missing value
print(maruthamunai_market)
print(maruthamunai_market.isna().sum())#check for missing values again
maruthamunai_market['season'].fillna('False', inplace=True)#filling missing value
print(maruthamunai_market)

maruthamunai_market['new'] = ['True','True','False','True',np.nan]#adding new column with missing value
print(maruthamunai_market)
print(maruthamunai_market.isna().sum())#check for missing values again
maruthamunai_market.dropna(inplace=True)#dropping missing values
print(maruthamunai_market)

maruthamunai_market['find'] = ['True','True','True',np.nan]#adding new column with missing value
print(maruthamunai_market)
print(maruthamunai_market.isna().sum())#check for missing values again
maruthamunai_market.dropna(axis=1, inplace=True)#dropping columns with missing values we can also use axis=0 for rows
print(maruthamunai_market)

#applying lambda function to a column
print(' ')
print('Applying lambda function to double the max values')
maruthamunai_market['max_double'] = maruthamunai_market['max'].apply(lambda x: x*2)
print(maruthamunai_market)

#data aggregation using groupby
data2= {'fruit': ['apple','banana','apple','banana','apple','banana'],
         'quantity': [10, 20, 15, 25, 30, 35],
         'price': [100, 200, 150, 250, 300, 350]}   
fruit_market= pd.DataFrame(data2)
print(' ') 
print('Fruit Market DataFrame:')
print(fruit_market)

count1= fruit_market['price'].count()#counting number of entries in price column
print(count1)

fruit_market_grouped= fruit_market.groupby('quantity').sum()#grouping by fruit and summing quantity and price
print(' ')
print('Fruit Market Grouped DataFrame:')
print(fruit_market_grouped)

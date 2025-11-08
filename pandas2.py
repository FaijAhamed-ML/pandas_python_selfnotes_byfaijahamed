import pandas as pd

data = {
    'vegetables': ['beetroot', 'carrot', 'tomato', 'kovakkai', 'coconut'],
    'color': ['purple', 'orange', 'red', 'green', 'white'],
    'unit': ['1kg', '1kg', '1kg', '500g', '1piece'],
    'min': [25, 35, 33, 40, 'seventeen'],
    'max': [40, 45, 90, 45, 38]
}

koyambed_market = pd.DataFrame(data)
print('koyambed_market DataFrame:')
print(koyambed_market)

print(' ')

data2 = {
    'vegetables': ['beetroot', 'carrot', 'redchili', 'beans', 'coconut'],
    'color': ['purple', 'orange', 'red', 'green', 'white'],
    'unit': ['1kg', '1kg', '1kg', '1kg', '1piece'],
    'min': [25, 35, 33, 40, 'seventeen'],
    'max': [40, 45, 90, 45, 38]
}

thiruvanmayoor = pd.DataFrame(data2)
print('thiruvanmayoor DataFrame:')
print(thiruvanmayoor)

print(' ')
#Merging DataFrames

merged_concat_rows = pd.concat([koyambed_market, thiruvanmayoor], axis=0) #Concatenation along rows
print('Merged DataFrame using concat:')
print(merged_concat_rows)

print(' ')
merged_concat_cols = pd.concat([koyambed_market, thiruvanmayoor], axis=1) #Concatenation along columns
print('Merged DataFrame using concat along columns:')
print(merged_concat_cols)

#Merging common columns
print(' ')
merged_inner = pd.merge(koyambed_market, thiruvanmayoor, on='vegetables', how='inner') #Inner join
print('Merged DataFrame using inner join:')
print(merged_inner)

print(' ')
merged_outer = pd.merge(koyambed_market, thiruvanmayoor, on='vegetables', how='outer') #Outer join
print('Merged DataFrame using outer join:')
print(merged_outer)

print(' ')
merged_left = pd.merge(koyambed_market, thiruvanmayoor, on='vegetables', how='left') #Left join
print('Merged DataFrame using left join:')
print(merged_left)

print(' ')
merged_right = pd.merge(koyambed_market, thiruvanmayoor, on='vegetables', how='right') #Right join
print('Merged DataFrame using right join:')
print(merged_right)
print(' ')

import pandas as pd 
df =pd.read_csv(r"c:\Users\hi\Downloads\Flavors.csv")
print("="*60)
print(df.head(10))

print(df['Base Flavor'])
grouped =   df.groupby('Base Flavor')

print("Count of each group")
print("= "*60)
print(grouped['Base Flavor'].count())
print("Mean of each group") 
print("= "*60)
#print(grouped['Base Flavor'].mean()) the mean only works on numeric columns, so it will not work on the Base Flavor column
print("Sum of each group")
print("= "*60)
print(grouped['Base Flavor'].sum())
print("Max of each group")
print("= "*60)
print(grouped['Base Flavor'].max())
print("Min of each group")
print("="*60)
print(grouped['Base Flavor'].min())
#for multiple columns, we can use the agg() function to get the mean, sum, max and min of each group
print("Mean, Sum, Max and Min of each group")
print("="*60)
print(df.groupby('Base Flavor').agg({'Flavor Rating':[ 'mean','sum', 'max', 'min'],'Texture Rating':['mean', 'sum', 'max', 'min']})) 

print("Mean, Sum, Max and Min for multiple columns")
print("="*60)
print(df.groupby(['Base Flavor', 'Liked']).agg({'Flavor Rating': ['mean', 'sum', 'max', 'min'], 'Texture Rating': ['mean', 'sum', 'max', 'min']}))


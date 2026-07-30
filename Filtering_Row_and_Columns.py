import pandas as pd
import openpyxl
df=pd.read_csv(r"c:\Users\hi\Downloads\world_population.csv")
print(df)
print(f"Shape:{df.shape}")
print(f"Col_Name:{df.columns}")

#To view ranks in the file less than rank 10
print(df[df['Rank']<10])

#To View the Specifc_columns
Specific_Country=['Bangladesh','Brazil']
print("Specific Country")
#To check if that country exists in the data we use .isin
print(df[df['Country'].isin(Specific_Country)])

#Another way of Checking 
print(df[df['Country'].str.contains('United ')])

#To set the index at single place
df2=df.set_index('Capital')
print("Single col")
print(df2)
df2.reset_index(inplace=True)# Before multi index_set make use reset otherwise it will show the previous indexing
# To set the index at multiple places
Multi_Col=df2.filter(items=['Country','Continent'] )
print("Multiple col ")
print(Multi_Col)

#To view from the rows 
print(df.iloc[1:])
#To view only Country & Capital from the data
print(df[['Country','Capital']])




















import pandas as pd
df=pd.read_csv(r"c:\Users\hi\Downloads\world_population.csv")
print(df)

# sorting single column in ASCENDING
print("SINGLE COL IN ASCENDING ORDER ")
asc=df.sort_values(by="Country")
print(asc)

#for sorting single column in DESCENDING
print("SINGLE COL IN DESCENDING ORDER ")
Dsc=df.sort_values(by="Country",ascending=False)
print(Dsc)

#for sorting multiple column in ASCENDING
print("Multiple COL IN ASCENDING ORDER ")
asc_multiple=df.sort_values(by=["Rank","Country"])
print(asc_multiple)

#for Sorting Multiple  column in DESCENDING
print("Multiple COL IN DESCENDING ORDER ")
Dsc_multiple=df.sort_values(by=["Rank","Country" ],ascending=[False,False])
print(Dsc_multiple)

#we can also use it  on a columns with specific need  in order by Ascending (or) Descending
#single
#1.single specific need column in Ascending order 
#2.single specific needcolumn in Descending order 
#Multiple
#3.Multiple  specific need Columns in Ascending order 
#4.Multiple  specific need Columns in Descending order
#5.Multiple specific need Columns in Ascending and Descending 
#6.Multiple specific need Columns in Descending and Ascending 

#1.single specific column in Ascending order
print("1.single specific column in Ascending order")
specific_col_asc=df[df['Rank']<20].sort_values(by='Rank') #By defualt it is set to the asc order 
print(specific_col_asc)

#2.single specific column in Descending order 
print("2.single specific column in Descending order")
specific_col_dsc=df[df['Rank']<20].sort_values(by='Rank',ascending=False) #By defualt it is set to the asc order 
print(specific_col_dsc)

#3.Multiple  specific columns in Ascending order
print("3.Multiple  specific columns in Ascending order")
specific_col_asc_Multi=df[df['Rank','Country']<20].sort_values(by=['Rank','Country'])
print(specific_col_asc_Multi)

#4.Multiple  specific columns in Descending order
print("4.Multiple  specific columns in Descending order")
specific_col_dsc_Multi=df[df['Rank','Country']<20].sort_values(by=['Rank','Country'],ascending=[False,False])# here we have to pass 2 parametes for Desc
print(specific_col_dsc_Multi)

#5.Multiple specific Columns in Ascending and Descending 
print("5.Multiple  specific columns in Ascending & Descending order")
specific_col_Asc_and_Dsc_Multi=df[df['Rank','Country']<20].sort_values(by=['Rank','Country'],ascending=[True,False])#True = Asc,False=Desc
print(specific_col_Asc_and_Dsc_Multi)

#6.Multiple  specific columns in Descending & Ascending order
print("6.Multiple  specific columns in Descending & Ascending order")
specific_col_Dsc_and_Asc_Multi=df[df['Rank','Country']<20].sort_values(by=['Rank','Country'],ascending=[False,True])
print(specific_col_Dsc_and_Asc_Multi)
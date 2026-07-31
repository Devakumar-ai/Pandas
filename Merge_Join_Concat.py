import pandas as pd

df = pd.read_csv(r"c:\Users\hi\Downloads\LOTR.csv")
print("Data Frame 1")

print("="*60)
print(df)
print("="*60)

df1=pd.read_csv(r"c:\Users\hi\Downloads\LOTR 2.csv")
print("Data Frame 2")

print("="*60)
print(df1)
print("="*60)
#merging  puts the table next to another
merg_in=df.merge(df1) # By Default it joins through  inner 
print("Merging on inner")
print("="*60)
print(merg_in)
print("="*60)
print("Merging on outer")
print("="*60)
merg_out=df.merge(df1,how='outer')
print(merg_out)
print("="*60)
print("Merging on left ")
print("="*60)
merg_left=df.merge(df1,how="left")
print(merg_left)
print("="*60)
print("Merging on right ")
print("="*60)
merg_right=df.merge(df1,how='right')
print(merg_right)
print("="*60)
print("Merging on Cross")
print("="*60)
merg_cross=df.merge(df1,how='cross')
print(merg_cross)
print("="*60)

print("                         JOINS                                    ")
print("="*60)
print("Outer_Join")
print("="*60)
Outer_Join=df.join(df1,on='FellowshipID',how='outer',lsuffix='_left',rsuffix='_Right')
print(Outer_Join)
print("="*60)
print("Joining by the indexs")
print("="*60)
df2=df.set_index('FellowshipID').join(df1.set_index('FellowshipID'),lsuffix='_left',rsuffix='_Right',how='outer')
print(df2)
print("="*60)


#-------Concat it puts ne data frame on another

print("                       Concat                         ") 
print("="*60)
concat=pd.concat((df,df1),join='outer',axis=1)
print(concat)












import pandas as pd
# To read Json file 
df=pd.read_json(r"c:\Users\hi\Downloads\json_sample.json") 
print(df)
print("HEAD IN JSON")
print(df.head())# ()-by defalut it give top 5 we can pass the parameter 
print(df.head(10))# for eg:-(10) now it give top 10
print("TAIL IN JSON")
print(df.tail())#by defalut it give bottom 5 we can pass the parameter 
print(df.tail(10))# for eg:-(10) now it give bottom 10
#TO SEE THE INFORMATION OF THE ENTIRE DATA :- COUNT OF ROWS AND COLUMN
print("INFO OF JSON ")
print(df.info())

#To Read a csv File
df=pd.read_csv(r"c:\Users\hi\Downloads\countries of the world.csv")
print(df)
print("HEAD IN CSV")
print(df.head())# ()-by defalut it give top 5 we can pass the parameter 
print(df.head(10))# for eg:-(10) now it give top 10
print("TAIL IN CSV")
print(df.tail())#by defalut it give bottom 5 we can pass the parameter 
print(df.tail(10))# for eg:-(10) now it give bottom 10
#TO SEE THE INFORMATION OF THE ENTIRE DATA :- COUNT OF ROWS AND COLUMN
print("INFO OF CSV ")
print(df.info())

#FOR READING EXCEL FILE 
import openpyxl
df=pd.read_excel(r"c:\Users\hi\Downloads\world_population_excel_workbook.xlsx",sheet_name='Sheet1')
print(df)
print("HEAD  IN EXCEL")
print(df.head())# ()-by defalut it give top 5 we can pass the parameter 
print(df.head(10))# for eg:-(10) now it give top 10
print("TAIL IN EXCEL")
print(df.tail())#by defalut it give bottom 5 we can pass the parameter 
print(df.tail(10))# for eg:-(10) now it give bottom 10
#TO SEE THE INFORMATION OF THE ENTIRE DATA :- COUNT OF ROWS AND COLUMN
print("INFO OF EXCEL ")
print(df.info())

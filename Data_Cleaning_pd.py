import pandas as pd

# Read Excel file
df = pd.read_excel(r'c:\Users\hi\Downloads\Customer Call List.xlsx')

line = "-" * 60

# -------------------------------------------------
# Remove duplicates and unwanted column
# -------------------------------------------------
print(line)
print("Removing Duplicates and Unwanted Column")
print(line)

df = (
    df.drop_duplicates()
      .drop(columns='Not_Useful_Column')
)

# -------------------------------------------------
# Standardize Last Name
# -------------------------------------------------
print(line)
print("Standardizing Last Names")
print(line)

df['Last_Name'] = df['Last_Name'].str.strip('123./_')

# -------------------------------------------------
# Standardize Phone Numbers
# -------------------------------------------------
print(line)
print("Standardizing Phone Numbers")
print(line)

df['Phone_Number'] = (
    df['Phone_Number']
      .astype(str)
      .str.replace(r'[|/]', '-', regex=True)
      .replace({'nan': '', 'N-a': ''})
)

# -------------------------------------------------
# Split Address
# -------------------------------------------------
df[['Street_Address', 'State', 'Zip_Code']] = (
    df['Address'].str.split(',', n=2, expand=True)
)

# -------------------------------------------------
# Standardize Yes/No Columns
# -------------------------------------------------
replace_dict = {
    'Yes': 'Y',
    'No': 'N'
}

df['Paying Customer'] = df['Paying Customer'].replace(replace_dict)
df['Do_Not_Contact'] = df['Do_Not_Contact'].replace(replace_dict)

# -------------------------------------------------
# Replace Missing Values
# -------------------------------------------------
df = (
    df.replace({'NaN': '', 'N/a': ''})
      .fillna('')
)

# -------------------------------------------------
# Remove Customers
# 1. Do Not Contact = Y
# 2. Phone Number is Empty
# -------------------------------------------------
df = df[
    (df['Do_Not_Contact'] != 'Y') &
    (df['Phone_Number'].str.strip() != '')
]

# -------------------------------------------------
# Reset Index
# -------------------------------------------------
df.reset_index(drop=True, inplace=True)

print(line)
print("Final Cleaned Data")
print(line)
print(df)

































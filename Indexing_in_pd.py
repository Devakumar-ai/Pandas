import pandas as pd

# Display all columns
pd.set_option("display.max_columns", None)

# Read CSV and set Country as index
df = pd.read_csv(
    r"C:\Users\hi\Downloads\world_population.csv",
    index_col="Country"
)

# -----------------------------
# Indexing by String
# -----------------------------
print("=" * 50)
print("Indexing by String")
print("=" * 50)

# Single row
print("\nSingle Country (Algeria):")
print(df.loc["Algeria"])

# Multiple rows
print("\nMultiple Countries:")
print(df.loc[["Algeria", "Angola"]])

# -----------------------------
# Indexing by Integer
# -----------------------------
print("\n" + "=" * 50)
print("Indexing by Integer")
print("=" * 50)

# First row
print(df.iloc[0])

# Third row
print("\nThird Row:")
print(df.iloc[2])

# -----------------------------
# MultiIndex
# -----------------------------
print("\n" + "=" * 50)
print("MultiIndex")
print("=" * 50)

# Reset index before creating MultiIndex
df = df.reset_index()

# Create MultiIndex
df = df.set_index(["Continent", "Country"])

# Sort index
df = df.sort_index()

print(df)

# Access a specific country in a continent
print("\nAfrica -> Algeria")
print(df.loc[("Africa", "Algeria")])

# Access all countries in Africa
print("\nAll African Countries")
print(df.loc["Africa"])



import pandas as pd

# Read CSV
df = pd.read_csv(r"C:\Users\hi\Downloads\world_population.csv")

# Display all columns (optional)
pd.set_option("display.max_columns", None)

print("=" * 60)
print("Original Data")
print("=" * 60)
print(df)

# ---------------------------------------------------
# Sorting Entire DataFrame
# ---------------------------------------------------

print("\n1. Single Column - Ascending")
print(df.sort_values(by="Country"))

print("\n2. Single Column - Descending")
print(df.sort_values(by="Country", ascending=False))

print("\n3. Multiple Columns - Ascending")
print(df.sort_values(by=["Rank", "Country"]))

print("\n4. Multiple Columns - Descending")
print(df.sort_values(by=["Rank", "Country"], ascending=[False, False]))

# ---------------------------------------------------
# Filter Data
# ---------------------------------------------------

top20 = df[df["Rank"] < 20]

print("\n" + "=" * 60)
print("Countries with Rank < 20")
print("=" * 60)

# 1. Ascending
print("\n1. Rank - Ascending")
print(top20.sort_values(by="Rank"))

# 2. Descending
print("\n2. Rank - Descending")
print(top20.sort_values(by="Rank", ascending=False))

# 3. Multiple - Ascending
print("\n3. Rank ↑  Country ↑")
print(top20.sort_values(by=["Rank", "Country"]))

# 4. Multiple - Descending
print("\n4. Rank ↓  Country ↓")
print(top20.sort_values(
    by=["Rank", "Country"],
    ascending=[False, False]
))

# 5. Rank Ascending, Country Descending
print("\n5. Rank ↑  Country ↓")
print(top20.sort_values(
    by=["Rank", "Country"],
    ascending=[True, False]
))

# 6. Rank Descending, Country Ascending
print("\n6. Rank ↓  Country ↑")
print(top20.sort_values(
    by=["Rank", "Country"],
    ascending=[False, True]
))
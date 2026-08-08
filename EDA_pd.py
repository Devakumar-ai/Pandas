import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# Load Data
# --------------------------------------------------
df = pd.read_csv(r'C:\Users\hi\Downloads\world_population.csv')

# Display numbers with 2 decimal places
pd.set_option('display.float_format', lambda x: f'{x:.2f}')


# --------------------------------------------------
# Basic Information
# --------------------------------------------------
print("\n========== DATA INFO ==========")
print(df.info())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== UNIQUE VALUES ==========")
print(df.nunique())


# --------------------------------------------------
# Top 15 Countries by Population
# --------------------------------------------------
print("\n========== TOP 15 POPULATED COUNTRIES ==========")

top_population = (
    df.nlargest(15, '2022 Population')
)

print(
    top_population[
        ['Country/Territory', '2022 Population']
    ]
)


# --------------------------------------------------
# Top 15 Countries by World Population Percentage
# --------------------------------------------------
print("\n========== TOP 15 WORLD POPULATION % ==========")

top_percentage = (
    df.nlargest(15, 'World Population Percentage')
)

print(
    top_percentage[
        ['Country/Territory', 'World Population Percentage']
    ]
)


# --------------------------------------------------
# Correlation
# --------------------------------------------------
print("\n========== CORRELATION ==========")

numeric_df = df.select_dtypes(include='number')
corr = numeric_df.corr()

print(corr)


# --------------------------------------------------
# Correlation Heatmap
# --------------------------------------------------
plt.figure(figsize=(12, 8))

sns.heatmap(
    corr,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    linewidths=0.5
)

plt.title('Population Correlation Heatmap')
plt.tight_layout()
plt.show()


# --------------------------------------------------
# Group By Continent
# --------------------------------------------------
print("\n========== POPULATION BY CONTINENT ==========")

continent_avg = (
    df.groupby('Continent')[numeric_df.columns]
      .mean()
      .sort_values('2022 Population', ascending=False)
)

print(continent_avg)


# --------------------------------------------------
# Population Trend by Continent
# --------------------------------------------------
population_columns = [
    '2022 Population',
    '2020 Population',
    '2015 Population',
    '2010 Population',
    '2000 Population',
    '1990 Population',
    '1980 Population',
    '1970 Population'
]

continent_population = (
    df.groupby('Continent')[population_columns]
      .mean()
      .sort_values('2022 Population', ascending=False)
)

print("\n========== CONTINENT POPULATION ==========")
print(continent_population)


# --------------------------------------------------
# Line Plot
# --------------------------------------------------
continent_population.T.plot(
    figsize=(12, 7),
    marker='o'
)

plt.title('Average Population by Continent')
plt.xlabel('Year')
plt.ylabel('Average Population')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# --------------------------------------------------
# Box Plot
# --------------------------------------------------
plt.figure(figsize=(16, 8))

continent_population.boxplot()

plt.title('Population Distribution by Continent')
plt.ylabel('Population')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()






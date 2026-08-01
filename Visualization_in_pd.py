import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------
# Load Dataset
# -------------------------------------
df = pd.read_csv(r"C:\Users\hi\Downloads\Ice Cream Ratings.csv")

# Set Date as Index
df = df.set_index("Date")

# Separator
line = "-" * 60

# Choose a style once
plt.style.use("tableau-colorblind10")


def show_plot(title):
    """Display plot with a separator."""
    print(line)
    print(title)
    plt.tight_layout()
    plt.show()


# -------------------------------------
# Line Graph
# -------------------------------------
df.plot(
    kind="line",
    title="Ice Cream Rating",
    xlabel="Date",
    ylabel="Scores",
    figsize=(10, 5)
)
show_plot("LINE GRAPH")


# -------------------------------------
# Bar Chart
# -------------------------------------
df.plot(
    kind="bar",
    title="Ice Cream Rating",
    xlabel="Date",
    ylabel="Scores",
    figsize=(10, 5)
)
show_plot("BAR CHART")


# -------------------------------------
# Stacked Bar Chart
# -------------------------------------
df.plot(
    kind="bar",
    stacked=True,
    title="Stacked Bar Chart",
    figsize=(10, 5)
)
show_plot("STACKED BAR CHART")


# -------------------------------------
# Scatter Plot
# -------------------------------------
df.plot.scatter(
    x="Texture Rating",
    y="Overall Rating",
    s=70,
    c="red",
    title="Texture vs Overall Rating"
)
show_plot("SCATTER PLOT")


# -------------------------------------
# Histogram
# -------------------------------------
df.plot.hist(
    bins=10,
    figsize=(8, 5),
    title="Histogram"
)
show_plot("HISTOGRAM")


# -------------------------------------
# Box Plot
# -------------------------------------
df.plot.box(
    figsize=(8, 5),
    title="Box Plot"
)
show_plot("BOX PLOT")


# -------------------------------------
# Area Chart
# -------------------------------------
df.plot(
    kind="area",
    figsize=(10, 5),
    title="Area Chart"
)
show_plot("AREA CHART")


# -------------------------------------
# Pie Chart
# -------------------------------------
df.plot.pie(
    y="Flavor Rating",
    figsize=(8, 8),
    autopct="%1.1f%%",
    title="Flavor Rating Distribution"
)
show_plot("PIE CHART")






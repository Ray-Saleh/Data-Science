import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
auto_mpg_df = pd.read_csv("auto-mpg.csv", encoding="ISO-8859-1")

# Convert 'horsepower' to numeric (replace '?' with NaN and drop missing values)
auto_mpg_df["horsepower"] = pd.to_numeric(auto_mpg_df["horsepower"], errors="coerce")
auto_mpg_df.dropna(subset=["horsepower"], inplace=True)

# Scatter plot: Weight vs. MPG, colored by Cylinders
plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=auto_mpg_df, x="weight", y="mpg", hue="cylinders", palette="viridis", alpha=0.7, edgecolor="black"
)

# Customize chart
plt.xlabel("Vehicle Weight (lbs)")
plt.ylabel("Miles Per Gallon (MPG)")
plt.title("Scatter Plot: Vehicle Weight vs. MPG by Cylinder Count")
plt.legend(title="Cylinders", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Save and show plot
plt.savefig("auto_mpg_scatter_plot.png")
plt.show()

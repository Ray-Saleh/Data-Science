import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (replace '10s0379.xlsx' with your actual file path)
xlsx_file_path = "Data.xlsx"
df_xlsx = pd.read_excel(xlsx_file_path, sheet_name="Data")

# Extract relevant columns
df_temperatures = df_xlsx.iloc[6:, [0, 1] + list(range(4, 16))]
df_temperatures.columns = [
    "State", "City", "January", "February", "March", "April", "May",
    "June", "July", "August", "September", "October", "November", "December"
]

# Drop rows with missing values in key columns
df_temperatures = df_temperatures.dropna(subset=["State", "City"]).reset_index(drop=True)

# Convert temperature columns to numeric values
temperature_cols = df_temperatures.columns[2:]
df_temperatures[temperature_cols] = df_temperatures[temperature_cols].apply(pd.to_numeric, errors="coerce")

# Fix city names by stripping spaces and making them lowercase
df_temperatures["City"] = df_temperatures["City"].str.strip().str.lower()

# Print available cities for debugging
print("Available Cities in Dataset:")
print(df_temperatures["City"].unique())

# Select cities and ensure they exist in the dataset
selected_cities = ["phoenix", "los angeles", "new york", "chicago", "miami"]
df_selected = df_temperatures[df_temperatures["City"].isin(selected_cities)]

# Print found cities for verification
print("\nSelected Cities Found in Data:")
print(df_selected["City"].unique())

# Plot the line chart
plt.figure(figsize=(10, 6))
for _, row in df_selected.iterrows():
    plt.plot(temperature_cols, row[temperature_cols], marker='o', label=row["City"].title())

plt.xlabel("Month")
plt.ylabel("Temperature (°F)")
plt.title("Monthly Record High Temperatures for Selected Cities")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)

# Save the chart
plt.savefig("chart1.png")
print("Chart 1 saved as chart1.png")
plt.show()


# ------------------- Chart 2: Month with Most Record Highs -------------------

# Find the highest temperature per month across all cities
highest_temps_per_month = df_temperatures[temperature_cols].max()

# Create bar chart
plt.figure(figsize=(10, 6))
highest_temps_per_month.plot(kind="bar", color="skyblue")

plt.xlabel("Month")
plt.ylabel("Highest Recorded Temperature (°F)")
plt.title("Month with the Most Record Highs Across All Cities")
plt.xticks(rotation=45)
plt.grid(axis="y")

# Save the chart as an image
plt.savefig("chart2.png")
print("Chart 2 saved as chart2.png")

plt.show()

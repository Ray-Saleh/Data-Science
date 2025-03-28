import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
ibm_df = pd.read_csv("IBM.csv", encoding="ISO-8859-1")

# Convert 'Date' column to datetime format
ibm_df['Date'] = pd.to_datetime(ibm_df['Date'])

# Sort by date to ensure proper line plotting
ibm_df = ibm_df.sort_values(by='Date')

# Plot the line chart
plt.figure(figsize=(12, 6))
sns.lineplot(data=ibm_df, x='Date', y='Close(t)', label='IBM Closing Price', color='blue')

# Adding Moving Averages for trend analysis
sns.lineplot(data=ibm_df, x='Date', y='MA20', label='20-Day MA', color='orange')
sns.lineplot(data=ibm_df, x='Date', y='MA50', label='50-Day MA', color='green')

# Customize chart
plt.xlabel("Date")
plt.ylabel("Stock Price (USD)")
plt.title("IBM Stock Price Over Time")
plt.legend()
plt.xticks(rotation=45)

# Save and show plot
plt.savefig("ibm_stock_line_chart.png")
plt.show()

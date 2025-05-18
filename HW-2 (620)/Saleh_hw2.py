import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1: Load the dataset
gold = pd.read_csv("daily_gold_rate.csv")

# Task 2: List data types & first 10 rows
print("Task 2 - Data Types:")
print(gold.dtypes)
print("\nTask 2 - First 10 Rows:")
print(gold.head(10))

# Task 3: Convert Date column to datetime & format rows 100-150
gold['Date'] = pd.to_datetime(gold['Date'])
print("\nRows 100-150 (US Date Format):")
print(gold.iloc[100:151]['Date'].dt.strftime('%m/%d/%Y'))

# Task 4: Extract USD values for 2020 & 2021
gold_2020_2021 = gold.loc[gold['Date'].dt.year.isin([2020, 2021]), 'USD'].values

# Task 4(i): Median gold rate in USD
print("\nMedian gold rate in USD (2020-2021):", np.median(gold_2020_2021))

# Task 4(ii): Sort in descending order
print("\nSorted USD gold prices (Descending):")
print(np.sort(gold_2020_2021)[::-1])

# Task 4(iii): Calculate range
print("\nRange of gold prices in USD:", np.ptp(gold_2020_2021))  # Peak-to-Peak

# Task 5: Fill missing CNY values (1985)
mask = (gold['Date'] >= '1985-01-01') & (gold['Date'] <= '1985-01-04') & (gold['CNY'].isna())
gold.loc[mask, 'CNY'] = gold.loc[mask, 'USD'] * 2.82
print("\nMissing CNY values filled using USD conversion rate.")

# Task 6: Extract 2021 data
gold_rate_2021 = gold[gold['Date'].dt.year == 2021].copy()

# Task 6(i): Monthly stats for INR
gold_rate_2021['Month'] = gold_rate_2021['Date'].dt.month
monthly_stats = gold_rate_2021.groupby('Month')['INR'].agg(['mean', 'max', 'min'])
print("\nMonthly INR stats (2021):")
print(monthly_stats)

# Task 6(ii): Lowest month for USD, EUR, INR
lowest_month = gold_rate_2021.groupby('Month')[['USD', 'EUR', 'INR']].idxmin()
print("\nMonth with lowest gold rate in USD, EUR, INR:")
print(lowest_month)

# Task 7: Add 'Remarks' column
def market_trend(row):
    prev_day = gold.loc[row.name - 1, 'GBP'] if row.name > 0 else row['GBP']
    next_day = gold.loc[row.name + 1, 'GBP'] if row.name < len(gold) - 1 else row['GBP']
    return 'gold rally' if row['GBP'] > prev_day and row['GBP'] > next_day else 'bearish gold market'

gold['Remarks'] = gold.apply(market_trend, axis=1)
print("Remarks column added based on GBP market trend.")

# Task 8: Aggregate yearly average gold rates
yearly_gold_rate = gold.drop(columns=['Remarks']).groupby(gold['Date'].dt.year).mean()

# Task 8(i): Plot gold price trend in EUR
plt.figure(figsize=(10, 5))
sns.lineplot(x=yearly_gold_rate.index, y=yearly_gold_rate['EUR'])
plt.title("Yearly Gold Rate in EUR")
plt.xlabel("Year")
plt.ylabel("Gold Rate in EUR")
plt.show()
print("\nLine chart plotted for yearly gold rate in EUR.")

# Task 8(ii): Identify sudden peaks/drops in gold price trends
price_diff = yearly_gold_rate['EUR'].diff()
sudden_changes = price_diff[price_diff.abs() > price_diff.std()]
print("\nYears with sudden peak/drop in gold price:")
print(sudden_changes)

# Task 8(ii): Explanation of sudden price changes
# Significant gold price changes occurred in the following years
# 2009: Increase due to the 2008 financial crisis, leading to investors seeking safe-haven assets
# 2011: Increase due to Eurozone debt crisis and high inflation fears.
# 2013: Decrease due to the Federal Reserve signaling a reduction in quantitative easing.
# 2020: Increase due to COVID-19 economic uncertainty, leading to a gold price surge.
# Sources: [World Gold Council](https://www.gold.org), [IMF Reports](https://www.imf.org), [Federal Reserve Publications](https://www.federalreserve.gov)."


# Task 9: Descriptive vs. Diagnostic Analysis
# Descriptive analysis focuses on summarizing past data, identifying trends, and visualizing information without drawing conclusions about causes.
# Examples: Listing data types, displaying rows, computing averages (Q1, Q2, Q3, Q6(i), Q8(i)).

# Diagnostic analysis aims to identify reasons behind patterns or anomalies in data, often using deeper investigation techniques.
# Examples: Finding median and range, analyzing missing values, trend identification, and anomaly explanation (Q4, Q5, Q6(ii), Q7, Q8(ii)).


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv', encoding='ISO-8859-1', header=[2, 3], skiprows=[0, 1])
df_density = df[[('Unnamed: 0_level_0', '  United States '), ('2009', '86.8')]].copy()
df_density.columns = ['State', '2009']
df_density = df_density[~df_density['State'].isin(['United States', 'District of Columbia'])]
df_density['2009'] = pd.to_numeric(df_density['2009'], errors='coerce')

plt.figure(figsize=(8, 5))
sns.histplot(df_density['2009'], bins=10)
plt.title('Population Density Distribution - 2009 (Histogram)')
plt.xlabel('Population Density (per sq. mile)')
plt.ylabel('Number of States')
plt.tight_layout()
plt.savefig("histogram.png")

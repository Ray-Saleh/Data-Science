
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def ecdf(data):
    x = np.sort(data)
    y = np.arange(1, len(x)+1) / len(x)
    return x, y

df = pd.read_csv('data.csv', encoding='ISO-8859-1', header=[2, 3], skiprows=[0, 1])
df_density = df[[('Unnamed: 0_level_0', '  United States '),
                 ('1980', '64.0'), ('2009', '86.8')]].copy()
df_density.columns = ['State', '1980', '2009']
df_density = df_density[~df_density['State'].isin(['United States', 'District of Columbia'])]
df_density['1980'] = pd.to_numeric(df_density['1980'], errors='coerce')
df_density['2009'] = pd.to_numeric(df_density['2009'], errors='coerce')

x_1980, y_1980 = ecdf(df_density['1980'].dropna())
x_2009, y_2009 = ecdf(df_density['2009'].dropna())

plt.figure(figsize=(8, 5))
plt.plot(x_1980, y_1980, marker='.', linestyle='none', label='1980')
plt.plot(x_2009, y_2009, marker='.', linestyle='none', label='2009')
plt.title('eCDF of Population Density (1980 vs 2009)')
plt.xlabel('Population Density (per sq. mile)')
plt.ylabel('ECDF')
plt.legend()
plt.tight_layout()
plt.savefig("ecdf.png")

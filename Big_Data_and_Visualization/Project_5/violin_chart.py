import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv('data.csv', encoding='ISO-8859-1', header=[2, 3], skiprows=[0, 1])
df_density = df[[('Unnamed: 0_level_0', '  United States '),
                 ('1970', '57.5'), ('1980', '64.0'),
                 ('2000', '79.6'), ('2009', '86.8')]].copy()
df_density.columns = ['State', '1970', '1980', '2000', '2009']
df_density = df_density[~df_density['State'].isin(['United States', 'District of Columbia'])]
for col in ['1970', '1980', '2000', '2009']:
    df_density[col] = pd.to_numeric(df_density[col], errors='coerce')
df_melted = df_density.melt(id_vars='State', var_name='Year', value_name='Density')
df_melted = df_melted.dropna()

# Create violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(data=df_melted, x='Year', y='Density', inner='box', scale='width')
plt.title('Population Density Distribution by Year (Violin Plot with Boxplot Inside)')
plt.xlabel('Year')
plt.ylabel('Population Density (per sq. mile)')
plt.tight_layout()
plt.savefig("violin.png")

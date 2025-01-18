import pandas as pd
import matplotlib.pyplot as plt

# Load the metadata file for visualization
data_path_metadata = './Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_900.csv'
data_path_population = './API_SP.POP.TOTL_DS2_en_csv_v2_900.csv'

# Load the data
metadata = pd.read_csv(data_path_metadata, sep=',', encoding='utf-8', on_bad_lines='skip')
population = pd.read_csv(data_path_population, sep=',', encoding='utf-8', skiprows=4, on_bad_lines='skip')

# Filter valid income group entries
metadata = metadata.dropna(subset=['IncomeGroup'])

# Bar chart: Distribution of countries by income group
income_group_counts = metadata['IncomeGroup'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(income_group_counts.index, income_group_counts.values, color='skyblue')
plt.title('Distribution of Countries by Income Group', fontsize=16)
plt.xlabel('Income Group', fontsize=14)
plt.ylabel('Number of Countries', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

# Bar chart: Distribution of countries by region
region_counts = metadata['Region'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(region_counts.index, region_counts.values, color='lightgreen')
plt.title('Distribution of Countries by Region', fontsize=16)
plt.xlabel('Region', fontsize=14)
plt.ylabel('Number of Countries', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

# Histogram: Population distribution in 2021 (log scale for better visualization)
population['2021'] = pd.to_numeric(population['2021'], errors='coerce')
population_2021 = population['2021'].dropna()
plt.figure(figsize=(10, 6))
plt.hist(population_2021, bins=30, color='orange', log=True, edgecolor='black')
plt.title('Population Distribution in 2021', fontsize=16)
plt.xlabel('Population', fontsize=14)
plt.ylabel('Frequency (log scale)', fontsize=14)
plt.tight_layout()
plt.show()

# Histogram: Yearly population growth rates (example: 2020 vs 2019)
population['2020'] = pd.to_numeric(population['2020'], errors='coerce')
population['2019'] = pd.to_numeric(population['2019'], errors='coerce')
population['GrowthRate_2020'] = (population['2020'] - population['2019']) / population['2019'] * 100

growth_rates = population['GrowthRate_2020'].dropna()
plt.figure(figsize=(10, 6))
plt.hist(growth_rates, bins=30, color='purple', edgecolor='black')
plt.title('Population Growth Rates (2020)', fontsize=16)
plt.xlabel('Growth Rate (%)', fontsize=14)
plt.ylabel('Frequency', fontsize=14)
plt.tight_layout()
plt.show()

# Additional bar chart: Top 10 most populous countries in 2021
top10_population = population[['Country Name', '2021']].dropna().sort_values(by='2021', ascending=False).head(10)
plt.figure(figsize=(10, 6))
plt.bar(top10_population['Country Name'], top10_population['2021'], color='red')
plt.title('Top 10 Most Populous Countries in 2021', fontsize=16)
plt.xlabel('Country', fontsize=14)
plt.ylabel('Population', fontsize=14)
plt.xticks(rotation=45, fontsize=12)
plt.tight_layout()
plt.show()

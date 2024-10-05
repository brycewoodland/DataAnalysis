import pandas as pd

# Load the data into a DataFrame
data = pd.read_csv('bear_attack_data.csv')

# Clean the data: remove rows with missing values in relevant columns
data_cleaned = data.dropna(subset=['Year', 'Type of bear'])

# Group by Year and Type of bear, then count the number of attacks
attacks_per_year = data_cleaned.groupby(['Year', 'Type of bear']).size().unstack(fill_value=0)

# Calculate mean and standard deviation for each type of bear
mean_attacks = attacks_per_year.mean()
std_attacks = attacks_per_year.std()

# Display the results
print("Mean attacks per year by bear type:")
print(mean_attacks)
print("\nStandard deviation of attacks per year by bear type:")
print(std_attacks)
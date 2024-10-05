import pandas as pd

# Load the data
bear_attacks = pd.read_csv('bear_attack_data.csv')

# Strip leading and trailing spaces
bear_attacks.columns = bear_attacks.columns.str.strip()

# Clean the data
bear_attacks_cleaned = bear_attacks.drop_duplicates()

# Remove rows with missing values
bear_attacks_cleaned = bear_attacks_cleaned.dropna(subset=['gender'])

# Remove trailing 'A' from gender entries
bear_attacks_cleaned['gender'] = bear_attacks_cleaned['gender'].str.replace(r'Â$', '', regex=True)

# Ensure each column contains only 'male' or 'female'
valid_genders = ['male', 'female']
bear_attacks_cleaned = bear_attacks_cleaned[bear_attacks_cleaned['gender'].isin(valid_genders)]

# Sort the data by gender
bear_attacks_cleaned = bear_attacks_cleaned.sort_values(by='gender')

# Filter through gender of victims for males
male_victims = bear_attacks[(bear_attacks['gender'] == 'male')]

# Filter through gender of victims for females
female_victims = bear_attacks[(bear_attacks['gender'] == 'female')]

# Display the total number of bear attacks on males
print(f"Total number of bear attacks for Male: {len(male_victims)}")

# Display the total number of bear attacks on females
print(f"Total number of bear attacks for Female: {len(female_victims)}")

# Calculate and display the percentage of attacks on males and females
total_victims = len(bear_attacks_cleaned)
male_victims_percentage = (len(male_victims) / total_victims) * 100
female_victims_percentage = (len(female_victims) / total_victims) * 100

print(f"Percentage of bear attacks on males: {male_victims_percentage:.2f}%")
print(f"Percentage of bear attacks on females: {female_victims_percentage:.2f}%")
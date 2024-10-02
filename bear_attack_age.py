import pandas as pd
import matplotlib.pyplot as plt

# Load the data.
bear_attacks = pd.read_csv('bear_attack_data.csv')

# Strip leading and trailing spaces.
bear_attacks.columns = bear_attacks.columns.str.strip()

# Clean the data.
bear_attacks_cleaned = bear_attacks.drop_duplicates()

# Remove rows with missing values.
bear_attacks_cleaned = bear_attacks_cleaned.dropna(subset=['age'])

# Filter through victims 0 - 18 years old.
young_victims = bear_attacks[bear_attacks['age'] <= 25]

# Filter through victims age 19 -59.
adult_victims = bear_attacks[(bear_attacks['age'] >= 26) & (bear_attacks['age'] <= 50)]

# Filter through victims age 60 and older.
elderly_victims = bear_attacks[bear_attacks['age'] >= 51]

# Display the total number of bear attacks.
print(f"Total number of bear attacks: {len(bear_attacks)}")

# Display the total number of young victims.
print(f"Total number of victims age 0 to 25: {len(young_victims)}")

# Display the total number of adult victims.
print(f"Total number of victims age 26 to 50: {len(adult_victims)}")

# Display the total number of elderly victims.
print(f"Total number of victims age 51 and older: {len(elderly_victims)}")

# # Histogram of bear attacks by age.
# bear_attacks['age'].plot(kind='hist', bins=10, color='blue', edgecolor='black')

# # Add labels and title.
# plt.xlabel('Age')
# plt.ylabel('Number of Victims')
# plt.title('Distribution of Bear Attacks by Age')

# # Display the histogram.
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Load the data.
bear_attacks = pd.read_csv('bear_attack_data.csv')

# # Count attacks per year.
# attacks_per_year = bear_attacks['Year'].value_counts().sort_index()

# # Plot the data.
# plt.figure(figsize=(12, 6))
# attacks_per_year.plot(kind='bar', color='skyblue')
# plt.title('Bear Attacks per Year')
# plt.xlabel('Year')
# plt.ylabel('Number of Attacks')
# plt.grid()
# plt.show()

# Count attacks by month
monthly_attacks = bear_attacks['Month'].value_counts().sort_index()

# Plot the data.
plt.figure(figsize=(12, 6))
monthly_attacks.plot(kind='bar', color='yellow')
plt.title('Bear Attacks by Month')
plt.xlabel('Month')
plt.ylabel('Number of Attacks')
plt.grid()
plt.show()
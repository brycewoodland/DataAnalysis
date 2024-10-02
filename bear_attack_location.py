import pandas as pd

# Load the data
bear_attacks = pd.read_csv('bear_attack_data.csv')

# Strip leading and trailing spaces
bear_attacks.columns = bear_attacks.columns.str.strip()

# Clean the data
bear_attacks_cleaned = bear_attacks.drop_duplicates()

# Remove rows with missing values
bear_attacks_cleaned = bear_attacks_cleaned.dropna(subset=['Location'])

# Filter through victims attacked in the woods from Location and Description columns
woods_victims = bear_attacks[bear_attacks['Location'].str.contains('woods', case=False) | bear_attacks['Description'].str.contains('woods', case=False)]

# Filter through victims attacked in the mountains from Location and Description columns
mountain_victims = bear_attacks[bear_attacks['Location'].str.contains('mountain', case=False) | bear_attacks['Description'].str.contains('mountain', case=False)]

# Filter through victims attacked in the park from Location and Description columns
park_victims = bear_attacks[bear_attacks['Location'].str.contains('park', case=False) | bear_attacks['Description'].str.contains('park', case=False)]

# Filter through victims attacked at the zoo from Location and Description columns
zoo_victims = bear_attacks[bear_attacks['Location'].str.contains('zoo', case=False) | bear_attacks['Description'].str.contains('zoo', case=False)]

# Filter through victims attacked in the river, lake, and sea/ocean from Location and Description columns
river_victims = bear_attacks[bear_attacks['Location'].str.contains('river', case=False) | bear_attacks['Location'].str.contains('lake', case=False) | bear_attacks['Location'].str.contains('sea', case=False) | bear_attacks['Location'].str.contains('ocean', case=False) | bear_attacks['Description'].str.contains('river', case=False) | bear_attacks['Description'].str.contains('lake', case=False) | bear_attacks['Description'].str.contains('sea', case=False) | bear_attacks['Description'].str.contains('ocean', case=False)]

# Display the total number of bear attacks in the river
print(f"Total number of bear attacks in the river: {len(river_victims)}")

# Display the total number of victims attacked in the woods
print(f"Total number of victims attacked in the woods: {len(woods_victims)}")

# Display the total number of victims attacked in the mountains
print(f"Total number of victims attacked in the mountains: {len(mountain_victims)}")

# Display the total number of victims attacked in the park
print(f"Total number of victims attacked in the park: {len(park_victims)}")

# Display the total number of victims attacked at the zoo
print(f"Total number of victims attacked at the zoo: {len(zoo_victims)}")

# Search for description that includes the word "camping".
camping_victims = bear_attacks[bear_attacks['Description'].str.contains('camping', case=False)]

# Display the total number of victims attacked while camping.
print(f"Total number of victims attacked while camping: {len(camping_victims)}")

# Search for description that includes the word "hiking".
hiking_victims = bear_attacks[bear_attacks['Description'].str.contains('hiking', case=False)]

# Display the total number of victims attacked while hiking.
print(f"Total number of victims attacked while hiking: {len(hiking_victims)}")

# Search for description that includes the word "fishing".
fishing_victims = bear_attacks[bear_attacks['Description'].str.contains('fishing', case=False)]

# Display the total number of victims attacked while fishing.
print(f"Total number of victims attacked while fishing: {len(fishing_victims)}")

# Search for description that includes the word "picnic".
picnic_victims = bear_attacks[bear_attacks['Description'].str.contains('picnic', case=False)]

# Display the total number of victims attacked while having a picnic.
print(f"Total number of victims attacked while having a picnic: {len(picnic_victims)}")

# Search for description that includes the word "biking".
biking_victims = bear_attacks[bear_attacks['Description'].str.contains('biking', case=False)]

# Display the total number of victims attacked while biking.
print(f"Total number of victims attacked while biking: {len(biking_victims)}")

# Search for description that includes the word "running".
running_victims = bear_attacks[bear_attacks['Description'].str.contains('running', case=False)]

# Display the total number of victims attacked while running.
print(f"Total number of victims attacked while running: {len(running_victims)}")

# Search for description that includes the word "skiing".
skiing_victims = bear_attacks[bear_attacks['Description'].str.contains('skiing', case=False)]

# Display the total number of victims attacked while skiing.
print(f"Total number of victims attacked while skiing: {len(skiing_victims)}")

# Search for description that includes the word "climbing".
climbing_victims = bear_attacks[bear_attacks['Description'].str.contains('climbing', case=False)]

# Display the total number of victims attacked while climbing.
print(f"Total number of victims attacked while climbing: {len(climbing_victims)}")

# Search for description that includes the word "hunting".
hunting_victims = bear_attacks[bear_attacks['Description'].str.contains('hunting', case=False)]

# Display the total number of victims attacked while hunting.
print(f"Total number of victims attacked while hunting: {len(hunting_victims)}")

# Display total number of victims attacked while camping, hiking, fishing, picnicking, biking, running, skiing, climbing, and hunting.
total_victims = len(camping_victims) + len(hiking_victims) + len(fishing_victims) + len(picnic_victims) + len(biking_victims) + len(running_victims) + len(skiing_victims) + len(climbing_victims) + len(hunting_victims)

# Search for description that includes the word "zoo".
zoo_victims = bear_attacks[bear_attacks['Description'].str.contains('zoo', case=False)]

# Display the total number of victims attacked while at the zoo.
print(f"Total number of victims attacked while at the zoo: {len(zoo_victims)}")

# Display the total number of victims attacked while camping, hiking, fishing, picnicking, biking, running, skiing, climbing, and hunting.
print(f"Total number of victims attacked while camping, hiking, fishing, picnicking, biking, running, skiing, climbing, and hunting: {total_victims}")
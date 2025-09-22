import csv
import random

# Define the list of countries and their weights
countries = ["Krasnodar", "Novosibirsk", "Kazan", "Moscow", "Sant Petersburg"]
weights = [1, 1, 1, 3, 2]  # Moscow and Sant Petersburg have 2x frequency

# Step 1: Read the existing CSV data
rows = []
with open("marketing_campaign.csv", "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  # Read the header row
    rows.append(header + ["Country"])  # Add "Country" to the header
    for row in reader:
        # Assign a country with weighted probability
        row.append(random.choices(countries, weights=weights, k=1)[0])
        rows.append(row)

# Step 2: Write the updated data back to the CSV file
with open("marketing_campaign.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(rows)

print("Column 'Country' added successfully with weighted randomness!")

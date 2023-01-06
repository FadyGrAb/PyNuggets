import csv
import json
import random
from pprint import pprint

# Docs
# CSV
# https://docs.python.org/3/library/csv.html
# JSON
# https://docs.python.org/3/library/json.html


# Initiate random data
machine = list(range(1, 101))
measurement_types = ["temp", "voltage", "current"]

print("="*50)
print("Read/Write CSV files".center(50))
print("="*50)

# Write csv file
with open("readings.csv", "w") as readings_file_csv:
    csv_dictwriter = csv.DictWriter(
        readings_file_csv,
        fieldnames=["machine_id", "measurement", "value"],  # Table headers
        lineterminator="\n"
    )
    csv_dictwriter.writeheader()

    for _ in range(20):  # Generate 20 values
        data = {
            "measurement": random.choice(measurement_types),
            "value": random.random() * 10,
            "machine_id": random.choice(machine)
        }   # Note the different order that the header but same values.
        csv_dictwriter.writerow(data)
        print(data)

# Read csv file
with open("readings.csv", "r") as readings_file_csv:
    csv_dictreader = csv.DictReader(readings_file_csv)
    csv_rows = list(csv_dictreader)
    print("\nNumber of rows:", len(csv_rows))
    for row in csv_rows:
        print(row["machine_id"], row["measurement"], row["value"])
    # Compare the read items with the generated items from the write step.

print('\n')
print("="*50)
print("Read/Write JSON files".center(50))
print("="*50)

# Write JSON
data = []
# Generate random JSON data
for _ in range(20):
    machine_id = random.choice(machine)
    num_of_measurements = random.randint(1, 3)
    measurements = random.choices(measurement_types, k=num_of_measurements)
    readings = dict()

    for measurement in measurements:
        readings[measurement] = random.random() * 10

    data.append(
        {
            "machine_id": machine_id,
            "readings": readings
        }
    )

pprint(data)

# Write to file
with open("readings.json", "w") as readings_file_json:
    json.dump(
        data,
        readings_file_json,
        indent=4
    )

# Read from file
with open("readings.json", "r") as readings_file_json:
    json_data = json.load(
        readings_file_json
    )

print("\n")
print("Number of rows:", len(json_data))
for row in json_data:
    print(row)
# Compare the read items with the generated items from the write step.

"""
Write a Python script that reads data from a CSV file and writes it to a JSON file.

Sample CSV File data.csv:
name,age,city
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
"""

import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# Example usage
if __name__ == "__main__":
    print("CSV to JSON Converter")
    csv_file = 'data/data.csv'
    json_file = 'data.json'

    csv_to_json(csv_file, json_file)

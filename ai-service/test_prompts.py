import json
import requests

with open('test_inputs/demo_records.json', 'r') as file:
    records = json.load(file)

for index, record in enumerate(records, start=1):

    print(f"\n--- Testing Record {index} ---")

    response = requests.post(
        'http://localhost:5000/describe',
        json=record
    )

    try:
        print(response.json())
    except:
        print("Invalid response received")
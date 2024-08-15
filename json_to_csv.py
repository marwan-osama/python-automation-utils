import json
import csv

def json_to_csv(json_file, csv_file):
    # Open the JSON file and load the data
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Open the CSV file for writing
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        
        # Write the header
        writer.writerow(['Key', 'Value'])
        
        # Write the key-value pairs
        def write_dict(d, parent_key=''):
            for k, v in d.items():
                full_key = f"{parent_key}.{k}" if parent_key else k
                if isinstance(v, dict):
                    write_dict(v, full_key)
                else:
                    writer.writerow([full_key, v])

        write_dict(data)

# Usage example
json_to_csv('ar_QA.json', 'ar_QA.csv')

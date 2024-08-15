import json

def merge_json_files(file1_path, file2_path, output_path):
    # Read the JSON files
    with open(file1_path, 'r', encoding="utf-8") as file1:
        data1 = json.load(file1)

    with open(file2_path, 'r', encoding="utf-8") as file2:
        data2 = json.load(file2)

    # Merge data2 into data1
    def merge_dicts(base, updates):
        for key, value in updates.items():
            if key not in base:
                # Add new keys
                base[key] = value
            elif isinstance(base[key], dict) and isinstance(value, dict):
                # Recursively merge dictionaries
                merge_dicts(base[key], value)
            elif base[key] is None:
                # Update if base value is None
                base[key] = value

    merge_dicts(data1, data2)

    # Write the merged data to the output file
    with open(output_path, 'w', encoding="utf-8") as output_file:
        json.dump(data1, output_file, indent=4)

# Usage
file1_path = 'ar_QA_JAIDAH_geely+CHEVY_scandipwa.json'  # Path to the first JSON file
file2_path = 'ar_QA_CHEVY_geely.json'  # Path to the second JSON file
output_path = 'ar_QA_JAIDAH_geely_final.json'  # Path to save the merged JSON file

merge_json_files(file1_path, file2_path, output_path)


import csv
import json

def convert_csv_to_json(csv_filename):
    """convert the data from the specifird cvs file to json format
    and save it to a file named 'data json'"""
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = [row for row in csv_reader]
        
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    except FileNotFoundError:
        print(f"File {csv_filename} not found.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

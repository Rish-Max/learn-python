import os
import json
import csv

JSON_FILE_PATH = "user.json"
CSV_FILE_PATH = "user.csv"

def json_to_csv(file_path, csv_file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, "r") as file:
        users = json.load(file)

        if len(users) == 0:
            print("No users")
        
        headers = list(users[0].keys())
        with open(csv_file_path, "w") as file:
            writer = csv.DictWriter(file,fieldnames=headers)
            writer.writeheader()
            writer.writerows(users)

                
                   

json_to_csv(JSON_FILE_PATH,CSV_FILE_PATH)

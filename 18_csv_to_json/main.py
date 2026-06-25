import os
import json
import csv

CSV_FILE_PATH = "user.csv"
JSON_FILE_PATH = "user.json"

def csv_to_json(csv_file_path, json_file_path):
    if not os.path.exists(csv_file_path):
        return

    with open(csv_file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        users = list(reader)

        if len(users) == 0:
            print("No users")
            return
        with open(json_file_path, "w", encoding="utf-8") as file:
            json.dump(users, file, indent=2)
            print("Users converted to JSON successfully.")

csv_to_json(CSV_FILE_PATH, JSON_FILE_PATH)
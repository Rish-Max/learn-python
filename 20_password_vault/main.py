import getpass
import csv
import os
import base64

PATH = "password_vault.csv"
FIELDNAMES = ["website", "username", "password"]

def encode_password(username,password):
    #Convert to bytes
    pass_bytes = ':'.join([username,password]).encode('utf-8')
    #Encode to base64
    return base64.b64encode(pass_bytes).decode('utf-8')

def decode_password(encoded_password):
    #Decode from base64
    pass_bytes = base64.b64decode(encoded_password.encode('utf-8'))
    #Convert to string
    username, password = pass_bytes.decode('utf-8').split(':')
    return username, password

def mask_password(password):
    masked_password = ''
    for index,char in enumerate(password):
        if index % 2 == 0:
            masked_password += '*'
        else:
            masked_password += char
    return masked_password

def initialize_vault_db():
    if not os.path.exists(PATH):
        with open(PATH, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(FIELDNAMES)

def save_password_to_db(website, username, password):
    with open(PATH, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([website, username, encode_password(username, password)])
    print("Password added successfully.")

def view_password_from_db():
    with open(PATH, "r") as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            username, password = decode_password(row[2])
            print(f"Website: {row[0]}, Username: {username}, Password: {mask_password(password)}")


def search_password_from_db(website):
    with open(PATH, "r") as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            if row[0] == website:
                username, password = decode_password(row[2])
                print(f"Website: {row[0]}, Username: {username}, Password: {mask_password(password)}")
                return
    print("Password not found.")

def main():
    initialize_vault_db()
    while True:
        print("Welcome to the password vault")
        print("1. Add password")
        print("2. View password")
        print("3. Search password")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            website = input("Enter website: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            save_password_to_db(website, username, password)
        elif choice == 2:
            view_password_from_db()
        elif choice == 3:
            website = input("Enter website: ")
            search_password_from_db(website)
        elif choice == 4:
            print("Thank you for using the password vault.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")


main()
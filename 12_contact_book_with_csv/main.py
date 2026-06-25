import csv
import os

PATH = "contact_book.csv"

def create_contact_book():
    if not os.path.exists(PATH):
        with open(PATH, "w", newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email"])
    return PATH

def add_contact(name, phone, email):
    with open(PATH, "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print("Contact added successfully.")

def view_all_contacts():
    with open(PATH, "r", newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

        if len(rows) < 1:
            print("No contacts found.")
            return
        for row in rows:
            print(f"Name: {row['Name']}, Phone: {row['Phone']}, Email: {row['Email']}")
        return


def search_contact(name):
    with open(PATH, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        for row in rows:
            if row['Name'].lower() == name.lower():
                print(f"Name: {row['Name']}, Phone: {row['Phone']}, Email: {row['Email']}")
                return
        print("Contact not found.")

def main():
    create_contact_book()
    while True:
        print("Welcome to the contact book")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == 2:
            view_all_contacts()
        elif choice == 3:
            name = input("Enter name: ").strip()
            search_contact(name)
        elif choice == 4:
            print("Thank you for using the contact book.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")
    

if __name__ == "__main__":
    main()

    
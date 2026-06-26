import json
import os
from datetime import datetime
from cryptography.fernet import Fernet

VAULT_FILE = "vault.json"
KEY_FILE = "vault.key"


def load_and_generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as file:
            file.write(key)
    else:
        with open(KEY_FILE, "rb") as file:
            key = file.read()
    return Fernet(key)

fernet = load_and_generate_key()

def load_data_from_vault():
    if not os.path.exists(VAULT_FILE):
        return []
    with open(VAULT_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_data_to_vault(data):
    with open(VAULT_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)


def add_todo_to_vault(title, content):
    data = load_data_from_vault()
    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data.append({"title": title, "content": encrypted_content, "timestamp": timestamp})
    save_data_to_vault(data)
    print("Todo added successfully.")

def view_todos_from_vault():
   data = load_data_from_vault()
   for todo in data:
      encrypted_content = todo['content']
      decrypted_content = fernet.decrypt(encrypted_content.encode()).decode()
      print(f"Title: {todo['title']}")
      print(f"Content: {decrypted_content}")
      print(f"Timestamp: {todo['timestamp']}")
      print("-" * 50)

def search_todo_in_vault(keyword):
   data = load_data_from_vault()
   for todo in data:
        if keyword.lower() in todo['title'].lower():
            encrypted_content = todo['content']
            decrypted_content = fernet.decrypt(encrypted_content.encode()).decode()
            print(f"Title: {todo['title']}")
            print(f"Content: {decrypted_content}")
            print(f"Timestamp: {todo['timestamp']}")
            print("-" * 50)
        else:
            print("No todos found with the keyword.")

def main():
    while True:
        print("Welcome to the todo vault")
        print("1. Add todo")
        print("2. View todos")
        print("3. Search todo")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            title = input("Enter the title: ")
            content = input("Enter the content: ")
            add_todo_to_vault(title, content)
        elif choice == 2:
            view_todos_from_vault()
        elif choice == 3:
            keyword = input("Enter the keyword: ")
            search_todo_in_vault(keyword)
        elif choice == 4:
            print("Thank you for using the todo vault.")
            break
        else:
            print("Invalid choice. Please enter a valid choice.")

if __name__ == "__main__":
    main()
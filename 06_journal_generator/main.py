import os 
import datetime

PATH = "journal.txt"

def append_to_journal(journal):
    if os.path.exists(PATH):
        with open(PATH, "a") as file:
            file.write(journal)
    else:
        with open(PATH, "w") as file:
            file.write(journal)
    print("Journal appended successfully.")

def gnerate_journal_content(content):
    current_date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"{current_date_time} - {content}\n"

def main():
    isExit = False
    while not isExit:
        journal = input("Enter the journal: ")
        content =gnerate_journal_content(journal)
        append_to_journal(content)
        isExit = input("Do you want to exit? (y/n): ") == "y"
        if isExit:
            isExit = True

main()
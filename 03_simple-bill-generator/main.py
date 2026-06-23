import datetime
print("Enter the details to generate bill")

current_date = datetime.date.today().strftime("%Y-%m-%d")
isExit = False

while not isExit:
    try:
        total_amount = float(input("Enter the total amount: ").strip())
        if total_amount <= 0:
            print("Invalid total amount. Please enter a valid total amount.")
            continue

        persons = input("Enter the persons separated by comma:").split(',')
        if len(persons) == 0:
            print("Invalid persons. Please enter a valid persons.")
            continue

        per_person_amount = total_amount / len(persons)

        print("\n")
        for person in persons:
            print(f"{person} owes {per_person_amount:.2f}")

        print("\n")
        print(f"Total amount: {total_amount}")
        print(f"Per person amount: {per_person_amount:.2f}")
        print("\n")

        print("Thank you for using the bill generator.")
        print(f"Generated on: {current_date}")
        isExit = True
    except ValueError:
        print("Invalid total amount. Please enter a valid total amount.")
    except Exception as e:
        print(f"An error occurred. {e}")
    finally:
        if isExit:
            print("Thank you for using the bill generator.")
        else:
            isExit = input("Do you want to exit? (y/n): ") == "y"
            if isExit:
                print("Thank you for using the bill generator.")    





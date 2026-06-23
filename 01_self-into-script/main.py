import datetime
isExit = False

while not isExit:
    print("Enter the details to generate self intro script")
    try:
        name = input("Enter your name: ").strip()
        age = int(input("Enter your age: ").strip())
        city = input("Enter your city: ").strip()

        current_date = datetime.date.today().strftime("%Y-%m-%d")
        script = f"Hello, my name is {name} and I am {age} years old. I live in {city}.\nGenerated on: {current_date}"
   

        print("\n--------------------------------")
        print(script)
        print("--------------------------------\n")

        isExit = True
    except ValueError as e:
        print(f"Invalid input. Please enter a valid age. {e}")
    except Exception as e:
        print(f"An error occurred. {e}")
    finally:
        if isExit:
            print("Thank you for using the self intro script generator.")
        else:
            isExit = input("Do you want to exit? (y/n): ") == "y"
            if isExit:
                print("Thank you for using the self intro script generator.")








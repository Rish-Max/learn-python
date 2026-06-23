import datetime
current_year = datetime.date.today().year
isExit = False

def calcclate_age(year_of_birth):    
    year_of_birth = current_year - year_of_birth
    month_of_birth = year_of_birth * 12
    day_of_birth = month_of_birth * 30
    hour_of_birth = day_of_birth * 24
    minute_of_birth = hour_of_birth * 60
    second_of_birth = minute_of_birth * 60
    week_of_birth = day_of_birth * 7

    return year_of_birth, month_of_birth, day_of_birth, hour_of_birth, minute_of_birth, second_of_birth, week_of_birth

def main():
    global isExit
    try:
        year_of_birth = float(input("Enter your year of birth: "))
        if year_of_birth <= 0 or year_of_birth > current_year:
            print("Invalid year of birth. Please enter a valid year of birth.")
            isExit = input("Do you want to exit? (y/n): ") == "y"
            if isExit:
                print("Thank you for using the age calculator.")
            else:
                main()

        year_of_birth, month_of_birth, day_of_birth, hour_of_birth, minute_of_birth, second_of_birth, week_of_birth = calcclate_age(year_of_birth)
        print(f"You are {int(year_of_birth)} years old.")
        print(f"You are {int(month_of_birth)} months old.")
        print(f"You are {int(day_of_birth)} days old.")
        print(f"You are {int(hour_of_birth)} hours old.")
        print(f"You are {int(minute_of_birth)} minutes old.")
        print(f"You are {int(second_of_birth)} seconds old.")
        print(f"You are {int(week_of_birth)} weeks old.")
    except ValueError as e:
        print(f"Invalid year of birth. Please enter a valid year of birth. {e}")
        isExit = input("Do you want to exit? (y/n): ") == "y"
        if isExit:
            print("Thank you for using the age calculator.")
        else:
            main()
    except Exception as e:
        print(f"An error occurred. {e}")
        isExit = input("Do you want to exit? (y/n): ") == "y"
        if isExit:
            print("Thank you for using the age calculator.")
        else:
            main()
    finally:
        if not isExit:
            isExit = input("Do you want to exit? (y/n): ") == "y"
            if isExit:
                print("Thank you for using the age calculator.")
            else:
                main()

main()
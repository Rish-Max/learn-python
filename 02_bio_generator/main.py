def save_bio(bio):
    with open("bio.txt", "w") as file:
        file.write(bio)
    print("Bio saved successfully.")

def generate_bio():
    print("Enter the details to generate bio")

    name = input("Enter your name: ").strip()
    profession = input("Enter your profession: ").strip()
    hobbies = input("Enter your hobbies: ").strip()
    website = input("Enter your website: ").strip()

    print(f"Enter the style of the bio you want to generate: ")

    isInvalidStyle = True
    while isInvalidStyle:
        style = int(input("Enter the style: 1 as formal, 2 as informal: ").strip())
        try:
            if 1 == style:
                bio = f"My name is {name} and I am {profession} by profession. My hobbies are {hobbies} and my website is {website}."
                isInvalidStyle = False
            elif 2 == style:
                bio = f"Hey, I'm {name} and I'm a {profession}. My hobbies are {hobbies} and my website is {website}."
                isInvalidStyle = False
            else:
                print("Invalid style. Please enter a valid style.")
        except ValueError:
            print("Invalid style. Please enter a valid style.")
        except Exception as e:
            print(f"Invalid style. Please enter a valid style. {e}")

    return bio

def main():
    bio = generate_bio()
    print("\n--------------------------------")
    print(bio)
    save_bio(bio)
    print("--------------------------------\n")
    print("Thank you for using the bio generator.")

main()


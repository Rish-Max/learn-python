def friendship_calculator(name1 : str, name2 : str):
    name1 = name1.lower()
    name2 = name2.lower()

    shared_letter = set(name1) & set(name2)
    max_len_name = max(len(name1), len(name2))
    vowels = set("aeiou")

    shared_letter_score  = len(shared_letter) * 10
    vowels_score = len(set(shared_letter) & vowels) * 5

    return min(shared_letter_score + vowels_score,100)


def main():
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    friendship_score = friendship_calculator(name1, name2)
    print(f"The friendship score between {name1} and {name2} is {friendship_score}")

main()
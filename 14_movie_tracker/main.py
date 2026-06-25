import os
import json

PATH = "movies.json"

def load_movies():
    if not os.path.exists(PATH):
        return []

    with open(PATH,'r') as f:
        return json.load(f)


def add_movie():
    title = input("Enter the movie name ")
    
    movies_list = load_movies()

    if any([movie for movie in movies_list if movie["title"] == title]):
        print('Movie already added')

    gnere = input("Enter the movie genere")
    try:
        rating = int(input("Enter the rating for movie"))

        if rating < 0 or rating >10:
            raise ValueError

    except ValueError:
        print("Rating can only be from 0 to 10")

    movies_list.append({"title":title,"gnere":gnere,"rating":rating})

    with open(PATH,'w',encoding='utf-8') as file:
        json.dump(movies_list,file,indent=2)

    
def view_movies():
    movies = load_movies()
    for movie in movies:
        print(f"Title : {movie['title']} Genre : {movie['gnere']} Rating: {movie['rating']}")


def main():
    while True:
        print(f"""
        1. Add movies
        2. View movies
        3. Exit
        """)
        choice = input("Enter the choice from 1 to 3")

        match choice:
            case "1": add_movie()
            case "2": view_movies()
            case "3": break
            case "4" : print("Invalid choice")


if __name__ == "__main__":
    main()
import os
import requests

PATH = "pokemon_info.csv"

def log_file():
    if not os.path.exists(PATH):
        with open(PATH, "w", encoding="utf-8") as file:
            file.write("Name, Experience, Weight\n")
    return PATH

def logger(info):
    with open(PATH, "a", encoding="utf-8") as file:
        file.write(info)
    print("Pokemon info logged successfully.")

def get_pokemon_info(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    if response.status_code == 200:
       return response.json()
    else:
        return None

def main():
    log_file()
    pokemon_name = input("Enter the pokemon name: ")
    info = get_pokemon_info(pokemon_name)
    
    if info == None:
        print("Pokemon not found.")
        return
    
    name = info["name"]
    experience = info["base_experience"]
    weight = info["weight"]
    logger(f"{name},{experience},{weight}\n")

if __name__ == "__main__":
    main()
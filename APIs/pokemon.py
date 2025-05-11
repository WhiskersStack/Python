import requests
import json
import metadata
import random
import os
import time

print("\n*** Welcome to the Pokémon API ***")


flag = True

def get_basic_pokemon_info(pokemon_id):

    url = metadata.BASE_URL + metadata.ENDPOINTS["pokemon"] + pokemon_id
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return

    data = response.json()

    print("\nRandom Pokémon Info : \n")

    i = 1
    if pokemon_id != "":
        print(f"ID : {data['id']}")
        print(f"Name : {data['name']}")
        print(f"Height : {data['height']} cm")
        print(f"Weight : {data['weight']} kg")
        print("Types : ")
        for t in data["types"]:
            print(f" - {t['type']['name']}")
        print("Abilities : ")
        for a in data["abilities"]:
            print(f" - {a['ability']['name']}")
    else:
        print("\nThe following Pokémon list will be saved in a file named 'pokemon_list.json' in the current directory :\n")
        
        pokemon_list = []
        i = 1

        for pokemon in data["results"]:
            pokemon_list.append(pokemon['name'])
            print(f"{i}. {pokemon['name']}")
            i += 1

        # Save the Pokémon list to a JSON file
        with open("pokemon_list.json", "w") as f:
            json.dump(pokemon_list, f, indent=4)

        print("\nPokémon list saved to 'pokemon_list.json'")

while flag:
    random_num = str(random.randint(1, 1000))
    is_draw = input("\n> Do you want to draw a Pokémon? (y/n): ").strip().lower()

    if is_draw == "y":
        print("\n**************************")
        print("Drawing a Pokémon, please wait...")
        for i in range(3, 0, -1):
            print(".")
            time.sleep(1)

        get_basic_pokemon_info(random_num)
    else:
        print("\n**************************")
        print("Fetching Pokémon list, please wait...")
        for i in range(3, 0, -1):
            print(".")
            time.sleep(1)

        get_basic_pokemon_info("")

    flag = input("\n> Do you want to continue? (y/n): ").strip().lower() == "y"
    if not flag:
        print("\n**************************")
        print("Goodbye, closing the program...")
        for i in range(3, 0, -1):
            print(".")
            time.sleep(1)
        print("\nDone!")
        break

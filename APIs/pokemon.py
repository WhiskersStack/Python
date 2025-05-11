import requests
import json
import metadata
import random

print("\n*** Welcome to the Pokémon API ***\n")

random_num = str(random.randint(1, 1000))


def get_basic_pokemon_info(pokemon_id):

    url = metadata.BASE_URL + metadata.ENDPOINTS["pokemon"] + pokemon_id
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return

    data = response.json()

    # basic_info = {
    #     "id": data["id"],
    #     "name": data["name"],
    #     "base_experience": data["base_experience"],
    #     "height": data["height"],
    #     "weight": data["weight"],
    #     "abilities": [a["ability"]["name"] for a in data["abilities"]],
    # }

    print("\n*** Pokémon Info ***\n")
    # for key, value in basic_info.items():
    #     print(f"{key}: {value}")

    # print(data['results'])

    # i = 1
    # for pokemon in data['results']:
    #     print(f"{i}. {pokemon['name']}")
    #     i += 1

    if pokemon_id != "":
        for key in data.keys():
            if key == "name":
                print(f"{key} - {data[key]}, {data['id']}")
    else:
        i = 1
        for pokemon in data["results"]:
            print(f"{i}. {pokemon['name']}")
            i += 1


is_draw = input("Do you want to draw a Pokémon? (y/n): ").strip().lower()

if is_draw == "y":
    get_basic_pokemon_info(random_num)
else:
    get_basic_pokemon_info("")

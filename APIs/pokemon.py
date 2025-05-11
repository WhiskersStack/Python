import requests
import json
import metadata

pokemon_id = '1'  # Bulbasaur
url = metadata.BASE_URL + metadata.ENDPOINTS["pokemon"] + pokemon_id

def get_basic_pokemon_info():
    response = requests.get(url)

    if response.status_code != 200:
        print("Error:", response.status_code)
        return

    data = response.json()

    basic_info = {
        "id": data["id"],
        "name": data["name"],
        "base_experience": data["base_experience"],
        "height": data["height"],
        "weight": data["weight"],
        "abilities": [a["ability"]["name"] for a in data["abilities"]],
    }

    print("\n📋 Basic Pokémon Info:")
    for key, value in basic_info.items():
        print(f"{key}: {value}")



get_basic_pokemon_info()

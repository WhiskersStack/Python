import requests


def get_basic_pokemon_info(pokemon_id_or_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id_or_name}/"
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
        "forms": [f["name"] for f in data["forms"]],
        "game_indices": [
            {"game_index": gi["game_index"], "version": gi["version"]["name"]}
            for gi in data["game_indices"]
        ],
    }

    print("\n📋 Basic Pokémon Info:")
    for key, value in basic_info.items():
        print(f"{key}: {value}")


# Example usage
get_basic_pokemon_info("clefairy")  # or use "1" for Bulbasaur

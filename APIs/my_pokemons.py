import json


def find_pokemon(id):
    with open("pokemon_list.json", "r") as f:
        data = json.load(f)

        for pokemon in data:
            if pokemon["id"] == id:
                print(f"\nPokémon found: {pokemon['name']}")
                print(f"ID: {pokemon['id']}")
                print(f"Height: {pokemon['height']} cm")
                print(f"Weight: {pokemon['weight']} kg")
                print("Types: ")
                for t in pokemon["types"]:
                    print(f" - {t['type']['name']}")
                print("Abilities: ")
                for a in pokemon["abilities"]:
                    print(f" - {a['ability']['name']}")
                return False
    print("\nPokémon not found")
    return data

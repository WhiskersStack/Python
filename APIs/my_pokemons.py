import json

def find_pokemon(id):
    with open("pokemon_list.json", "r") as f:
        data = json.load(f)

        for pokemon in data:
            if pokemon["id"] == id:
                print(f"\nPokémon found: {pokemon['name']}")
                return pokemon
    print("\nPokémon not found")


find_pokemon(723)
find_pokemon(73)
find_pokemon(725)

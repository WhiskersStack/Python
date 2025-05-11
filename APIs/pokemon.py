import requests
import json
import metadata
import random
import os
import time


print("\n*** Welcome to the Pokémon API ***")

flag = True


# Get the Pokémon list from the API
def get_basic_pokemon_info(pokemon_id):
    url = (
        metadata.BASE_URL + metadata.ENDPOINTS["pokemon"] + pokemon_id
    )  # Base URL + Pokémon endpoint + Pokémon ID
    response = requests.get(url)  # Pokémon API request

    # Check if the response is successful
    if response.status_code != 200:
        print("Error:", response.status_code)
        return

    # Saving the response to a JSON file
    data = response.json()

    print("\nRandom Pokémon Info : \n")

    # If a Pokémon ID is provided, print its details
    if pokemon_id != "":
        print(f"id : {data['id']}")
        print(f"Name : {data['name']}")
        print(f"Height : {data['height']} cm")
        print(f"Weight : {data['weight']} kg")
        print("Types : ")
        for t in data["types"]:
            print(f" - {t['type']['name']}")
        print("Abilities : ")
        for a in data["abilities"]:
            print(f" - {a['ability']['name']}")
    # If no Pokémon ID is provided, print the list of Pokémon
    else:
        print(
            "\nThe following Pokémon list will be saved in a file named 'pokemon_list.json' in the current directory :\n"
        )

        pokemon_list = []  # List to store Pokémon names
        i = 1
        # Loop through the results and print the Pokémon names
        for pokemon in data["results"]:
            pokemon_list.append(pokemon["name"])
            print(f"{i}. {pokemon['name']}")
            i += 1

        # Save the Pokémon list to a JSON file
        with open("pokemon_list.json", "w") as f:
            json.dump(pokemon_list, f, indent=4)

        print("\nPokémon list saved to 'pokemon_list.json'")


# Interactive loop to ask the user if they want to draw a Pokémon or fetch the list, and continue or exit
while flag:
    random_num = str(
        random.randint(1, 1000)
    )  # Generate a random Pokémon ID between 1 and 1000
    is_draw = (
        input("\n> Do you want to draw a Pokémon? (y/n): ").strip().lower()
    )  # Ask the user if they want to draw a Pokémon

    # Check if the user input is valid
    if is_draw == "y":  # If the user wants to draw a Pokémon
        print("\n**************************")
        print("Drawing a Pokémon, please wait...")
        for i in range(3, 0, -1):
            print(".")
            time.sleep(1)

        get_basic_pokemon_info(
            random_num
        )  # Call the function to get Pokémon info with the random ID
    else:  # If the user doesn't want to draw a Pokémon
        print("\n**************************")
        print("Fetching Pokémon list, please wait...")
        for i in range(3, 0, -1):
            print(".")
            time.sleep(1)

        get_basic_pokemon_info(
            ""
        )  # Call the function to get Pokémon list with an empty ID

    # Ask the user if they want to continue or exit
    flag = input("\n> Do you want to continue? (y/n): ").strip().lower() == "y"
    if not flag:  # If the user doesn't want to continue
        print("\n**************************")
        print("Goodbye, closing the program...")

        for i in range(3, 0, -1):
            print(".")
            time.sleep(1)

        print("\nDone!⚡")
        break  # End of the program

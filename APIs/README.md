# Pokémon API Explorer 🧪

A simple Python script that interacts with the [PokéAPI](https://pokeapi.co/) to fetch and display information about Pokémon. Draw a random Pokémon or generate a list of the first 20 Pokémon and save them to a JSON file.

## 🧰 Project Structure

```
.
├── pokemon.py            # Main script to run the app
├── metadata.py           # API base URL and endpoint configuration
├── pokemon_list.json     # Output file for list of Pokémon (generated at runtime)
├── .gitignore            # Python-related ignores
```

## 🚀 Features

- Fetch detailed data for a **random Pokémon**
- Retrieve and save a **list of Pokémon names**
- Display Pokémon ID, name, height, weight, types, and abilities
- Store names to `pokemon_list.json` for reference

## 🔧 Requirements

- Python 3.x
- Internet connection

Install dependencies:

```bash
pip install requests
```

## ▶️ How to Run

Run the main script:

```bash
python pokemon.py
```

Then follow the on-screen prompts:

- `y` → draw a random Pokémon
- `n` → download the first 20 Pokémon names
- Continue or exit as you like

## 📦 Example Output

```
Do you want to draw a Pokémon? (y/n): y

Drawing a Pokémon, please wait...
.
.
.

Random Pokémon Info : 

ID : 25
Name : pikachu
Height : 4 cm
Weight : 60 kg
Types : 
 - electric
Abilities : 
 - static
 - lightning-rod
```

## 📁 pokemon_list.json

If you choose to fetch the list, the file will be saved with 20 Pokémon names like:

```json
[
  "bulbasaur",
  "ivysaur",
  "venusaur",
  ...
]
```

## 🧠 Notes

- The script uses `random.randint(1, 1000)` to fetch random Pokémon.
- The API call uses endpoints defined in `metadata.py` for cleaner structure.
- Loading animations use `time.sleep(1)` for a better UX.

## 🔒 License

This project uses the PokéAPI under their free use policy. No affiliation with Nintendo or Pokémon.

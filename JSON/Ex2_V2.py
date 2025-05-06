import json

# Challenge 2: Mini Movie Database

print("\n~~~ Challenge 2: Mini Movie Database ~~~\n")

# Read the JSON file
with open("movies.json", "r") as file:
    data = json.load(file)

# Search for a movie by title
user_movie = input("Enter a movie title you want to search : ")

# Initialize variables
new_movie_exist = False
id = 10
movie_found = False

# Search for the movie in the JSON data
for movie in data["movies"]:
    if movie["title"].lower() == user_movie.lower():
        movie_found = True
        print(f"\n~~~ {movie['title']} Found! ~~~\n")
        print("Details :\n")
        print(f"Director: {movie['director']}")
        print(f"Rating: {movie['rating']}")
        print("Genres :")
        for genre in movie["genres"]:
            print(f"         {genre}")
        break

# If the movie is not found, print a message
if not movie_found:
    print(f"\n{user_movie} not found in the database!")

# Add a new movie to the JSON data
new_movie = "Shrek"

print("\n~~~ Adding the Shrek movie ~~~\n")
print("\nSearching for the movie...\n")

# Check if the movie already exists in the JSON data
for movie in data["movies"]:
    if movie["title"].lower() == new_movie.lower():
        new_movie_exist = True
        print(f"\n~~~ {movie['title']} already in the list! ~~~\n")

# If the movie does not exist, add it to the JSON data
if not new_movie_exist:
    print(f"\n~~~ {new_movie} not found! ~~~\n")
    data["movies"].append(
        {
            "id": id + 1,
            "title": "Shrek",
            "director": "Andrew Adamson",
            "rating": 7.9,
            "genres": ["Animation", "Adventure", "Comedy"],
        }
    )
    print(f"\n~~~ The {new_movie} added to the database! ~~~\n")

# Update the JSON file with the new movie
    with open("movies.json", "w") as file:
        json.dump(data, file, indent=4)


# print(data)

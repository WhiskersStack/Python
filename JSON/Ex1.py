import json

# Exercise 1: Basic JSON Practice
book_found = False
id = 2

print("\n~~~ Exercise 1: Basic JSON Practice ~~~")

with open("books.json", "r") as file:
    data = json.load(file)


for book in data["books"]:
    print(
        f"\nTitle: {book['title']}, Average Ratings: {sum(book['ratings']) / len(book['ratings'])}"
    )

# print(data['books'][0]['title'])
# print(sum(data["books"][0]["ratings"]) / len(data["books"][0]["ratings"]))


for book in data["books"]:
    if book["title"] == "The Great Gatsby":
        print(f"\nFound the book : {book['title']}, it wont be added\n")
        book_found = True
        break


if not book_found:
    data["books"].append(
        {
            "id": id + 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "ratings": [4, 5, 3, 4, 5],
        }
    )
    print(f"\nAdded the book : The Great Gatsby\n")

print(data)

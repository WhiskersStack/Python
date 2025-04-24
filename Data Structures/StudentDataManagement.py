#  Student Data Management


print("\nWelcome to the Student Data Management!")

students = {
    "Alice": {
        "age": 20,
        "subjects": ["Math", "Science", "Sports"],
        "grades": {40, 50, 0},
    },
    "Bob": {
        "age": 22,
        "subjects": ["Math", "Science", "Sports"],
        "grades": {50, 60, 0},
    },
    "Charlie": {
        "age": 23,
        "subjects": ["Math", "Science", "Sports"],
        "grades": {60, 70, 0},
    },
}

students["David"] = {
    "age": 24,
    "subjects": ["Math", "Science", "Sports"],
    "grades": {70, 80, 0},
}

students["Bob"]["grades"] = {55, 60, 0}
del students["Charlie"]["subjects"][0]

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(students)
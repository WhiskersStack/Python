#  Student Data Management


print("\nWelcome to the Student Data Management!\n")

students = {
    "Alice": {
        "age": 20,
        "subjects": ["Math", "Science", "Sports"],
        "grades": {40, 50, 0},
    },
    "Bob": {
        "age": 22,
        "subjects": ["Math", "Science", "Sports"],
        "grades": {50, 60, 10},
    },
    "Charlie": {
        "age": 23,
        "subjects": ["Math", "Science", "Sports"],
        "grades": {60, 70, 0},
    },
    "John": {
        "age": 21,
        "subjects": ["Math", "Science", "Sports"],
        "grades": {89, 99, 80},
    },
}

students["David"] = {
    "age": 24,
    "subjects": ["Math", "Science", "Sports"],
    "grades": {70, 80, 0},
}

students["Bob"]["grades"] = {55, 60, 5}
del students["Charlie"]["subjects"][0]

bob_grades = list(students["Bob"]["grades"])

bob_average = int(sum(bob_grades) / len(bob_grades))
print(f"Bob's average grade is: {bob_average}")

highest_average = 0
for student in students.keys():
    grades = list(students[student]["grades"])
    average = int(sum(grades) / len(grades))
    if average > highest_average:
        highest_average = average
        student_name = student

# ~~~
print("\n***\n")
print(f"{student_name} has the highest average grade of: {highest_average}")
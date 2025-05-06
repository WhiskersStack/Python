import json

#  Exercise 2: Challenging JSON Practice

print("\n~~~ Exercise 2: Challenging JSON Practice ~~~")

id = 2

with open("students.json", "r") as file:
    data = json.load(file)


# Finding the student with the highest average score
for student in data["students"]:
    average_score = sum(student["scores"]) / len(student["scores"])
    highest_average_score = 0
    student["status"] = "participant"

    if average_score > highest_average_score:
        highest_average_score = average_score
        student_with_highest_average = student["name"]

# Adding the 'Winner' status to the student with the highest average score
for student in data["students"]:
    if student["name"] == student_with_highest_average:
        student["status"] = "Winner"
        break

data["students"].append(
    {
        "id": id + 1,
        "name": "John Cena",
        "scores": [4, 5, 3],
        "status": "participant",
    }
)

with open("students.json", "w") as file:
    json.dump(data, file, indent=4)

print(f"\n{data['students']}")

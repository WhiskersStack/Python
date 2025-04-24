# Managing a Dictionary

print("\nWelcome to the Dictionary Manager!")

students = {
    "Alice": {"age": 20, "grade": "40"},
    "Bob": {"age": 22, "grade": "50"},
    "Charlie": {"age": 23, "grade": "60"},
}

students["David"] = {"age": 24, "grade": "70"}
students["Bob"]["grade"] = "55"
del students["Charlie"]

print("\nThe students in the dictionary are:\n")

for key in students.keys():
    print(f"{key}: {students[key]}")

counter = 0
highest_grade = 0
grade_sum = 0

for key in students.keys():

    grade_sum = int(students[key]["grade"]) + grade_sum
    counter += 1

    if int(students[key]["grade"]) > highest_grade:
        highest_grade = int(students[key]["grade"])
        student_name = key

average_grade = grade_sum / counter

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"\nThe average grade is: {average_grade}")
print(
    f"The student with the highest grade is: {student_name} with a grade of {highest_grade}"
)

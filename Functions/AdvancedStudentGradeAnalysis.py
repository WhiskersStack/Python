# Advanced Student Grade Analysis

print("\n\n\n\n\n\n~~~ Advanced Student Grade Analysis ~~~\n")

students = [
    {"name": "Alice", "grades": [85, 90, 78]},
    {"name": "Bob", "grades": [92, 88, 84]},
    {"name": "Charlie", "grades": [70, 75, 80]},
    {"name": "Diana", "grades": [14, 13, 67]},
    {"name": "Eve", "grades": [45, 65, 33]},
]


average = list(
    map(
        lambda student: (
            student["name"],
            sum(student["grades"]) / len(student["grades"]),
        ),
        students,
    )
)


print(f"{'Name'.ljust(7)} | {'Average'}")
print("-" * 17)

for student in average:
    print(f"{student[0].ljust(7)} : {student[1]:.2f}")

print(f"\n{average}")

passed = list(filter(lambda student: student[1] > 50, average ))

print(f"{passed[0][1]}")
fgjfjffjfg
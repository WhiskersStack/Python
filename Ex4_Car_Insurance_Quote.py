# Ex4 : Car Insurance Quote

print("\nExercise 4 : Car Insurance Quote\n")

age = int(input("Enter your age: \n"))
accidents = int(input("Enter the number of accidents you had in the last 5 years: \n"))

if age < 25:
    price = 3000
else:
    price = 2000

if accidents > 0:
    price += accidents * 500

if price > 5000:
    print("High Risk")
else:
    print("Standard Risk")
print(f"Your insurance quote is: ${price}")
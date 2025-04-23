#  Check Even or Odd
#  This program checks if a number is even or odd.

print("\nWelcome to the Even or Odd Checker!")
print("This program will tell you if a number is even or odd.\n")

number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"\n~ {number} is even ~")
else:
    print(f"\n~ {number} is odd ~")


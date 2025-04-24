#  Numbers Divisible by 3

print("\nNumbers Divisible by\n")

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
divider = int(input("Enter the number to divide by: "))
counter = 0
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

for number in range(start, end + 1):
    if number % divider == 0:
        print(f"\n{number}")
        counter += 1
    

print(f"\n{counter} numbers are divisible by {divider} between {start} and {end}.")
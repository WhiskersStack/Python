# Calculator

# This is a simple calculator program that performs basic arithmetic operations.

def calc():
    print("\nWelcome to the calculator!\n")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("\nError: Division by zero is not allowed.")  
            return
    else:
        print("\nError: Invalid operation.")
        return

    print(f"\nThe result of {num1} {operation} {num2} is: {result}")    
calc()

# This program is a simple calculator that performs addition, subtraction, multiplication, and division.
# Its reliability is based on the correctness of the arithmetic operations and the handling of invalid inputs.
# The program is designed to be user-friendly and provides clear instructions for the user to follow.
import random

#  Guessing Game

print("\nWelcome to the Guessing Game!")

# Generate a random number between 1 and 20
random_number = random.randint(1, 20)
print(
    f"\nA random number between 1 and 20 has been generated: {random_number}"
)  # For testing purposes

user_number = None
attempts = 0

# Loop until the user guesses the correct number
while (user_number != random_number) and attempts < 5:
    print(f"\n~ Attempt {attempts + 1}/5 ~")
    # Get user input
    user_input = input("\nGuess a number between 1 and 20: ")

    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    # Validate input
    if not user_input.isdigit():
        print("Please enter a valid number.")
        continue

    user_number = int(user_input)
    attempts += 1

    # Check if the guess is too low, too high, or correct
    if user_number < random_number:
        print("\nToo low! Try again.")
    elif user_number > random_number:
        print("\nToo high! Try again.")
    else:
        print(
            f"\nCongratulations! You've guessed the number {random_number} in {attempts} attempts."
        )

    if attempts == 5 and user_number != random_number:
        print(f"\nGame over! The correct number was {random_number}.")

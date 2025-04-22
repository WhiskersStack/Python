import random
# Boxing Simulator

print("\nWelcome to the Boxing Simulator!\n")
print("Choose a move : 'jab', 'cross', 'hook', or 'uppercut'.")
print("\n~~~ Rules ~~~\n")
print("Jab (1) > Cross (2) > Hook (3)")
print("Hook (3) > Uppercut (4)")
print("Uppercut (4) > Jab (1)")
print("The first fighter to land 3 punches wins the match.\n")
print("Let's get started!\n")


score = 0
computer_score = 0

while score < 3 and computer_score < 3:
    user_move = int(input("Enter your move number (1 = Jab, 2 = Cross, 3 = Hook, 4 = Uppercut): "))

    computer_move = random.randint(1, 4)

    if computer_move == 1:
        computer_move_temp = "Jab"
    elif computer_move == 2:
        computer_move_temp = "Cross"
    elif computer_move == 3:
        computer_move_temp = "Hook"
    elif computer_move == 4:
        computer_move_temp = "Uppercut"

    if user_move == 1:
        user_move_temp = "Jab"
    elif user_move == 2:
        user_move_temp = "Cross"
    elif user_move == 3:
        user_move_temp = "Hook"
    elif user_move == 4:
        user_move_temp = "Uppercut"

    print("\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(f"Your move : {user_move_temp}")
    print(f"Computer's move : {computer_move_temp}")

    if user_move == computer_move:
        print(f"It's a tie!")
        score += 1
        computer_score += 1
    elif user_move == 1 and (computer_move == 2 or computer_move == 3):
        print(f"You won!")
        score += 1
    elif user_move == 2 and computer_move == 3:
        print(f"You won!")
        score += 1
    elif user_move == 3 and computer_move == 4:
        print(f"You won!")
        score += 1
    elif user_move == 4 and computer_move == 1:
        print(f"You won!")
        score += 1
    else:
        print(f"You lost!")
        computer_score += 1
    print(f"Score: You {score} - Computer {computer_score}\n")

if score > computer_score:
    print("Congratulations! You won the match!")
elif score < computer_score:
    print("Sorry! You lost the match.")
else:
    print("It's a draw!")

print("\nThank you for playing the Boxing Simulator!")
print("Goodbye!")
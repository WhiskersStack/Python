# Ex6 Wizard’s Final Exam

print("\nExercise 6 : Wizard’s Final Exam\n")

print("Welcome to the Wizard's Final Exam!")

spell_power = int(input("Enter your spell power (1-100): \n"))
spell_accuracy = int(input("Enter your spell accuracy (1-100): \n"))
spell_control = int(input("Enter your spell control (1-100): \n"))

average_score = (spell_power + spell_accuracy + spell_control) / 3
print(f"\nYour average score is: {average_score}")

if spell_accuracy < 40 or spell_control < 40 or spell_power < 40:
    print("You have failed the exam.")
else:
    if average_score >= 90:
        print("Archmage")
    elif average_score > 75 and average_score < 89:
        print("Mage")
    elif average_score > 50 and average_score < 74:
        print("Apprentice")
    else:
        print("Failed the exam")

        
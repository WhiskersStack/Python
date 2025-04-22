# Ex 3 : Medieval Guard Duty

print("\nExercise 3 : Medieval Guard Duty\n")
print("Im the mighty guard of the castle!")
print("I will let you in if you are a royal or if you have a gold pass, and at least 18 years old.")
print("But if you are on the blacklist, you are not allowed to enter the castle.")

age = int(input("\nEnter your age: \n"))
gold_pass = input("Do you have a gold pass? (True/False)\n")
is_royal = input("Are you a royal? (True/False)\n")
isBlacklist = input("Are you on the blacklist? (True/False)\n")

if age >= 18 and (gold_pass == "True" or is_royal == "True") and isBlacklist == "False":
    print("\nYou are allowed to enter the castle.")
    print("Welcome to the castle!")
    print("Enjoy your stay!")
else:
    print("\nYou are not allowed to enter the castle.")
    print("Go away!")
    print("You are not welcome here.")
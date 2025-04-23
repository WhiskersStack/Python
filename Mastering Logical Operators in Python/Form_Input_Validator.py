# Form Input Validator

print("\nForm Input Validator")

username = input("Enter your username: ")
password = input("Enter your password: ")
email = input("Enter your email: ")

if username and (len(password) >= 8 and any(char.isdigit() for char in password)) and (email.count("@") == 1 and email.endswith(".com")):
	print("\nAll inputs are valid!")
else:
	print("\nInvalid input. Please check your username, password, or email.")
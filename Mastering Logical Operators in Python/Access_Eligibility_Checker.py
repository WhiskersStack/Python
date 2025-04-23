# Part 3: Access Eligibility Checker

print("\nAccess Eligibility Checker\n")

print("This program checks if a user is eligible for access to a system based on their age and security clearance level.\n")

age = int(input("Enter your age: "))
has_ticket = input("Do you have a security clearance ticket? (yes/no): ").strip().lower()
vip_code = input("Enter your VIP code (if any): ").strip()

if age >= 0:
    if (age >= 18 and has_ticket == "yes") or vip_code == "GOLDVIP":
        print("\nAccess granted.")
    else:
        print("\nAccess denied.")
else:
    print("\nInvalid age entered. Please enter a valid age.")


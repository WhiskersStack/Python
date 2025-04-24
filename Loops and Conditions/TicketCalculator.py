# Movie‑Night Ticket Calculator

print("\nWelcome to the Movie-Night Ticket Calculator!")

age = int(input("\nEnter your age: "))
day = input("\nEnter if it's a weekday or weekend: ").strip().lower()
loyalty_card = input("\nDo you have a loyalty card? (y/n): ").strip().lower()
base_price = 20

if age < 0:
    print("\nInvalid age. Please enter a valid age.")
elif day not in ["weekday", "weekend"]:
    print("\nInvalid day. Please enter 'weekday' or 'weekend'.")
else:
    if age <= 13:
        ticket_price = base_price * 0.5
    elif age >= 60:
        ticket_price = base_price * 0.7
    else:
        ticket_price = base_price

    if day == "weekend":
        ticket_price += 5

    if loyalty_card == "y":
        ticket_price -= 2

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print(f"The ticket price is: ${ticket_price:.2f}")
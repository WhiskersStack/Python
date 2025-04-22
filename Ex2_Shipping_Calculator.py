# Ex 2 Shipping Calculator

print("\nExercise 2 : Shipping Calculator\n")

print("Welcome to the cup shop!")
print("We have a special offer for you:")
print("Each cup costs $15")
print("You can buy as many cups as you want")
print("Shipping cost is $50, unless the order is over $200, then shipping is free")
print("If the order is over $500, then 10% discount applied\n")


numberOfCups = int(input("How many cups do you want to buy? \n"))
if numberOfCups <= 0:
    print("Invalid number of cups. Please enter a positive number.")
    exit()
pricePerCup = 15
totalCost = numberOfCups * pricePerCup
shippingCost = 50

if totalCost > 200:
    shippingCost = 0

if totalCost > 500:
    discount = totalCost * 0.10
    totalCost -= discount
    print(f"\nDiscount of 10% applied: ${discount}")

totalCost += shippingCost

print(f"Total cost of the order is: ${totalCost}")
print(f"Shipping cost is: ${shippingCost}")
import json

print("\n~~~ Market Stock Manager ~~~")

with open("stock.json", "r") as file:
    data = json.load(file)

print("\nPriting the stocks in the database :")

i = 1
for stock in data:
    print(f"\n{i}. {stock['name']} - {stock['stock']} pcs")
    i += 1

i= 1
print("\nStocks with more than 50 pcs :")
for stock in data:
    if stock["stock"] > 50:
        print(f"\n{i}. {stock['name']}")
        i += 1

import json

print("\n~~~ Market Stock Manager ~~~")

with open("stock.json", "r") as file:
    data = json.load(file)


for stock in data:
    print(f"\nName : {stock['name']}")

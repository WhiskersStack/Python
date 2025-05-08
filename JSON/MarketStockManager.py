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

i = 1
print("\nStocks with less than 20 pcs :")
for stock in data:
    if stock["stock"] < 20:
        print(f"\n{i}. {stock['name']}")
        i += 1

print("\n****************************************")
category = input("\nEnter the category you want to search : ").lower()

i = 1
print("\nStocks in the category :")
for stock in data:
    if stock["category"].lower() == category:
        print(f"\n{i}. {stock['name']}")
        i += 1

print("\n****************************************")
min_price = float(input("\nEnter the minimum price : "))
max_price = float(input("\nEnter the maximum price : "))


i = 1
print("\nStocks in the price range :")
for stock in data:
    if float(stock["price"]) >= min_price and float(stock["price"]) <= max_price:
        print(f"\n{i}. {stock['name']}")
        i += 1

def find_product_by_name(name):
    stock_name = name.lower()
    for stock in data:
        if stock["name"].lower() == stock_name:
            return stock
    return None

print("\n****************************************\n")
print("Searching for an apple... :")
print(find_product_by_name("apple"))
print("\nSearching for a banana... :")
print(find_product_by_name("banana"))
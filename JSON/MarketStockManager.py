import json

print("\n~~~ Market Stock Manager ~~~")

with open("stock.json", "r") as file:
    data = json.load(file)

print("\nPriting the stocks in the database :")

i = 1
for stock in data:
    print(f"\n{i}. {stock['name']} - {stock['stock']} pcs")
    i += 1

i = 1
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


def is_unique_id(stock_id):
    for stock in data:
        if stock["id"] == stock_id:
            return False
    return True


print("\n****************************************\n")
print("Checking if the id 1 is unique... :")
print(is_unique_id(1))
print("\nChecking if the id 11 is unique... :")
print(is_unique_id(11))


def add_stock():
    id = int(input("\nEnter the id of the stock : "))
    name = input("\nEnter the name of the stock : ")
    category = input("\nEnter the category of the stock : ")
    price = float(input("\nEnter the price of the stock : "))
    stock = int(input("\nEnter the stock of the stock : "))

    if is_unique_id(id) and price > 0 and stock > 0:
        data.append(
            {
                "id": id,
                "name": name,
                "category": category,
                "price": price,
                "stock": stock,
            }
        )
    else:
        print("\n~~~ The stock already exists or the price/stock is invalid! ~~~\n")
        return

    print(f"\n~~~ The {name} added to the database JSON file! ~~~\n")
    #with open("stock.json", "w") as file:
        #json.dump(data, file, indent=4)


# add_stock()

print("\n****************************************\n")
print("Updating banana(id:2) stock... :")


def update_stock(id, new_stock):
    for stock in data:
        if stock["id"] == id and new_stock > 0:
            stock["stock"] = new_stock
            print("\nStock updated successful!\n")
            #with open("stock.json", "w") as file:
                #json.dump(data, file, indent=4)
            return

    print("\nError updating stock...\n")


update_stock(2, 33)


print("\n****************************************\n")
print("Increasing Bakery stock by 10... :")
def restock(category, num):
    for stock in data:
        if stock["category"].lower() == category.lower():
            stock["stock"] += num


restock("Bakery", 10)


print("\n****************************************\n")
del_category = input("Enter The category You want to delete : ")
i = 0
deleted = False
for stock in data:
    if stock["category"].lower() == del_category.lower():
        print(f"\n{stock['name']} deleted successful!")
        del data[i]
    i += 1

if not False:
    print("\nStock not found...\n")

with open("stock.json", "w") as file:
    json.dump(data, file, indent=4)

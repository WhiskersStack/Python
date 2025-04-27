######################################################

greetList = []

def greet(list):
    for name in list:
        print(f"Hello, {name}!")
        greetList.append(f"Hello, {name}!")


name1 = ["John", "Jane", "Doe"]
name2 = ["Alice", "Bob", "Charlie"]

print("\nGreeting from name1:")
greet(name1)

print("\nGreeting from name2:")
greet(name2)

print("\nGreeting from greet list:")
for greeting in greetList:
    print(greeting)

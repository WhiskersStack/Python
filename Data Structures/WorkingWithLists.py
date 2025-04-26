# Working with Lists

print("\nWorking with Lists")

tenNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tenNumbers.append(11)
tenNumbers.remove(5)
tenNumbers.insert(3, 2)

sum = sum(tenNumbers)

highest = max(tenNumbers)
lowest = min(tenNumbers)

print(f"\nSum: {sum}, Highest: {highest}, Lowest: {lowest}")
print(f"\nList: {tenNumbers}")
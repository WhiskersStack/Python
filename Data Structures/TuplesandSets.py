# Working with Tuples and Sets

print("\nWorking with Tuples and Sets\n")

num_set = {1, 2, 3, 4, 5}
num_tuple = (1, 4, 9, 16, 25)

num_list = list(num_set)
num_list.sort(reverse=True)
print(f"Sorted List: {num_list}")

for num in num_list:
    for i in num_tuple:
        if num == i:
            print(f"Number {num} is in both the set and tuple.")


print(f"\nLength of the set: {len(num_set)}, Length of the tuple: {len(num_tuple)}")

# You can't add or remove elements from a tuple, but you can do so with a set.
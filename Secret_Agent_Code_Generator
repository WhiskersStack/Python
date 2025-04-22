# Secret Agent Code Generator

print("Secret Agent Code Generator\n")

code1 = input("Enter a single word (letters only): \n")
code2 = input("Enter a single word (letters only): \n")
code3 = input("Enter a single word (letters only): \n")
numA = int(input("Enter a integer number: \n"))
numB = int(input("Enter a integer number: \n"))

if code1.isalpha() and code2.isalpha() and code3.isalpha() and numA > 0 and numB > 0:
    print("\nGood\n")
else:
    print("\nInvalid input, exiting...")
    exit()

combine = code1 + "-" + code2 + "-" + code3
secret_number = (numA * numB) + numA - numB
swapped_A = numB
swapped_B = numA
avg_value = (numA + numB) / 2
message_length = len(combine)
is_palindrome = combine == combine[::-1]

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"\nSecret Code : {combine}")
print(f"Secret Number : {secret_number}")
print(f"Swapped A : {swapped_A}, Swapped B : {swapped_B}")
print(f"Average Value : {avg_value}")
print(f"Combine Length : {message_length}")
print(f"Is Palindrome : {is_palindrome}")

# Reverse a String

print("\nReverse a String\n")


def reverse_string(text):
    print("Running reverse_string()")
    print("Original String: ", text)

    return text[::-1]

print("Reversed String: ", reverse_string("Hello, World!"))
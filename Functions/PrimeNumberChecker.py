# Prime Number Checker

print("\nPrime Number Checker\n")

num = 7
divider = [2, 3, 4, 5, 6, 7, 8, 9]

def is_prime(n):
    print("Running is_prime()")
    if n < 2:
        return False
    for i in divider:
        if n % i == 0 and n != i:
            return False
    return True

print("\nIs the number", num, "prime ?", is_prime(num))
#  Fibonacci Sequence Generator

print("\nFibonacci Sequence Generator\n")

n = 5  # Number of terms in the Fibonacci sequence


def fibonacci(n):
    print("Running fibonacci()")
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_term)
    return fib_sequence


print("\nFibonacci sequence up to", n, "terms:")
print(fibonacci(n))


def fibonacci_recursive(n, fib_sequence, i):

    if i == n:
        return fib_sequence

    next_term = fib_sequence[i - 1] + fib_sequence[i - 2]
    fib_sequence.append(next_term)
    i = i + 1
    fibonacci_recursive(n, fib_sequence, i)

    return fib_sequence


print("\nRec Func\n")
print(fibonacci_recursive(n, [0, 1], 2))

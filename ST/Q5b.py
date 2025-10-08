import timeit

# -------------------------------
# Fibonacci Implementations
# -------------------------------

# 1. Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

# 2. Iterative Fibonacci
def fib_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

# -------------------------------
# Benchmarking using timeit
# -------------------------------

# Set the input number
n = 20

# Measure recursive version
time_recursive = timeit.timeit(lambda: fib_recursive(n), number=1)
print(f"Recursive Fibonacci({n}) took {time_recursive:.6f} seconds")

# Measure iterative version
time_iterative = timeit.timeit(lambda: fib_iterative(n), number=1)
print(f"Iterative Fibonacci({n}) took {time_iterative:.6f} seconds")

# Compare results
if time_recursive > time_iterative:
    print("Iterative version is faster.")
else:
    print("Recursive version is faster.")

import tracemalloc

# -------------------------------
# Function to test memory usage
# -------------------------------
def create_large_list(n):
    """Create a list of squares from 1 to n."""
    return [i * i for i in range(1, n+1)]

# -------------------------------
# Track memory usage
# -------------------------------
tracemalloc.start()  # Start tracking memory

# Run the function
n = 100000
result = create_large_list(n)

# Take a snapshot of memory usage
current, peak = tracemalloc.get_traced_memory()

print(f"List of {n} elements created.")
print(f"Current memory usage: {current / 1024:.2f} KB")
print(f"Peak memory usage: {peak / 1024:.2f} KB")

tracemalloc.stop()  # Stop tracking memory

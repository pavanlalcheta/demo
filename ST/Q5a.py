import time
import unittest

# -------------------------------
# Function to test
# -------------------------------
def compute_squares(n):
    """Compute sum of squares from 1 to n."""
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

# -------------------------------
# Function to measure execution time
# -------------------------------
def measure_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# ============================================
# Unit Tests
# ============================================
class TestPerformance(unittest.TestCase):

    def test_compute_squares_result(self):
        """Test if compute_squares returns correct sum."""
        result, _ = measure_time(compute_squares, 5)  # 1^2+2^2+3^2+4^2+5^2 = 55
        self.assertEqual(result, 55)

    def test_execution_time_small_input(self):
        """Test execution time for small input."""
        _, exec_time = measure_time(compute_squares, 10)
        self.assertLess(exec_time, 0.01)  # Should be very fast

    def test_execution_time_large_input(self):
        """Test execution time for larger input."""
        _, exec_time = measure_time(compute_squares, 10000)
        self.assertLess(exec_time, 1)  # Should complete within 1 second

# ============================================
# Run Unit Tests
# ============================================
if __name__ == "__main__":
    unittest.main()

# ============================================
# Alpha/Beta Testing - A/B Test Evaluator
# ============================================

import unittest

class ABTestEvaluator:
    """Evaluator for comparing two versions of a feature."""
    
    def __init__(self):
        self.data = {"A": {"success": 0, "total": 0}, "B": {"success": 0, "total": 0}}

    def log_result(self, version, success):
        """Log a result for a version.
        success: True if the user converted, False otherwise
        """
        if version not in self.data:
            raise ValueError("Invalid version. Use 'A' or 'B'.")
        self.data[version]["total"] += 1
        if success:
            self.data[version]["success"] += 1

    def conversion_rate(self, version):
        """Return the conversion rate for the version."""
        if self.data[version]["total"] == 0:
            return 0.0
        return self.data[version]["success"] / self.data[version]["total"]

    def compare(self):
        """Compare versions and return the better version."""
        rate_a = self.conversion_rate("A")
        rate_b = self.conversion_rate("B")
        if rate_a > rate_b:
            return "A"
        elif rate_b > rate_a:
            return "B"
        else:
            return "Tie"


# ============================================
# Unit Tests for A/B Test Evaluator
# ============================================

class TestABTestEvaluator(unittest.TestCase):

    def setUp(self):
        self.evaluator = ABTestEvaluator()

    def test_log_result_and_conversion_rate(self):
        """Test logging results and calculating conversion rates."""
        self.evaluator.log_result("A", True)
        self.evaluator.log_result("A", False)
        self.evaluator.log_result("B", True)
        self.assertAlmostEqual(self.evaluator.conversion_rate("A"), 0.5)
        self.assertAlmostEqual(self.evaluator.conversion_rate("B"), 1.0)

    def test_compare_versions(self):
        """Test comparison between version A and B."""
        self.evaluator.log_result("A", True)
        self.evaluator.log_result("A", True)
        self.evaluator.log_result("B", True)
        self.evaluator.log_result("B", False)
        # Both have 50% conversion
        self.assertEqual(self.evaluator.compare(), "Tie")

        # Make B better
        self.evaluator.log_result("B", True)
        self.assertEqual(self.evaluator.compare(), "B")

    def test_invalid_version(self):
        """Test that logging an invalid version raises an error."""
        with self.assertRaises(ValueError):
            self.evaluator.log_result("C", True)


# ============================================
# Run Unit Tests (Simulating Alpha/Beta Testing)
# ============================================

if __name__ == "__main__":
    unittest.main()

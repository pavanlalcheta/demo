import unittest

# -------------------------------
# Simulated API Client
# -------------------------------
class APIClient:
    def __init__(self):
        # Simulated "API data"
        self.api_data = {
            "users": [
                {"name": "Alice", "age": 25},
                {"name": "Bob", "age": 30},
                {"age": 40}  # Missing name
            ],
            "error": None  # Can be set to simulate API error
        }

    def fetch_data(self, endpoint):
        """Simulate fetching data from API"""
        if endpoint == "error" or self.api_data.get(endpoint) is None:
            raise ValueError("API returned error")
        return self.api_data[endpoint]

    def process_data(self, data):
        """Extract 'name' field from the data"""
        return [item['name'] for item in data if 'name' in item]

# -------------------------------
# Unit Tests
# -------------------------------
class TestAPIClient(unittest.TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_fetch_data_success(self):
        """Test successful data fetch"""
        data = self.client.fetch_data("users")
        expected = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 30},
            {"age": 40}
        ]
        self.assertEqual(data, expected)

    def test_fetch_data_error(self):
        """Test API error handling"""
        with self.assertRaises(ValueError) as context:
            self.client.fetch_data("error")
        self.assertIn("API returned error", str(context.exception))

    def test_process_data(self):
        """Test processing of fetched data"""
        data = self.client.fetch_data("users")
        processed = self.client.process_data(data)
        self.assertEqual(processed, ["Alice", "Bob"])

# -------------------------------
# Run Unit Tests
# -------------------------------
if __name__ == "__main__":
    unittest.main()

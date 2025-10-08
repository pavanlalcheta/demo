import unittest
import os

# -------------------------------
# File Processing System
# -------------------------------
class FileProcessor:
    def read_file(self, filename):
        with open(filename, 'r') as f:
            return f.readlines()

    def process_data(self, data):
        # Convert lines to uppercase
        return [line.upper() for line in data]

    def write_file(self, filename, data):
        with open(filename, 'w') as f:
            f.writelines(data)

# -------------------------------
# Unit Tests
# -------------------------------
class TestFileProcessor(unittest.TestCase):

    def setUp(self):
        # Initialize processor and create input file
        self.processor = FileProcessor()
        self.input_file = 'test_input.txt'
        self.output_file = 'test_output.txt'
        with open(self.input_file, 'w') as f:
            f.write("hello\nworld\n")

    def tearDown(self):
        # Remove files after test
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_file_processing(self):
        # Read input
        data = self.processor.read_file(self.input_file)
        self.assertEqual(data, ["hello\n", "world\n"])

        # Process data
        processed = self.processor.process_data(data)
        self.assertEqual(processed, ["HELLO\n", "WORLD\n"])

        # Write output
        self.processor.write_file(self.output_file, processed)
        self.assertTrue(os.path.exists(self.output_file))

        # Verify written content
        with open(self.output_file, 'r') as f:
            result = f.readlines()
        self.assertEqual(result, ["HELLO\n", "WORLD\n"])

# -------------------------------
# Run Unit Tests
# -------------------------------
if __name__ == "__main__":
    unittest.main()

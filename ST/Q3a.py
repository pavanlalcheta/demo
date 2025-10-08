import unittest

# -------------------------------
# Simple Login System
# -------------------------------
class LoginSystem:
    def __init__(self):
        # Sample users database: username -> password
        self.users = {
            "admin": "admin123",
            "user1": "pass1",
            "user2": "pass2"
        }

    def login(self, username, password):
        """Return True if login successful, False otherwise"""
        if username in self.users and self.users[username] == password:
            return True
        return False

# -------------------------------
# Unit Tests for System Testing
# -------------------------------
class TestLoginSystem(unittest.TestCase):

    def setUp(self):
        self.system = LoginSystem()

    def test_correct_login(self):
        """Test login with correct username and password"""
        self.assertTrue(self.system.login("admin", "admin123"))
        self.assertTrue(self.system.login("user1", "pass1"))

    def test_incorrect_password(self):
        """Test login with incorrect password"""
        self.assertFalse(self.system.login("admin", "wrongpass"))
        self.assertFalse(self.system.login("user2", "1234"))

    def test_nonexistent_user(self):
        """Test login with a username that does not exist"""
        self.assertFalse(self.system.login("unknown", "pass"))

    def test_empty_username_password(self):
        """Test login with empty username or password"""
        self.assertFalse(self.system.login("", ""))
        self.assertFalse(self.system.login("admin", ""))
        self.assertFalse(self.system.login("", "admin123"))

# -------------------------------
# Run Unit Tests
# -------------------------------
if __name__ == "__main__":
    unittest.main()

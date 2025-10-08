# ===============================
# Alpha Testing - Internal Bug Reporting System
# ===============================

import unittest

class Bug:
    """Represents a single bug entry."""
    def __init__(self, bug_id, title, description):
        self.bug_id = bug_id
        self.title = title
        self.description = description
        self.status = "Open"

    def resolve(self):
        self.status = "Resolved"


class BugReportingSystem:
    """Internal system for logging and managing bugs."""
    def __init__(self):
        self.bugs = {}

    def add_bug(self, bug_id, title, description):
        if bug_id in self.bugs:
            raise ValueError("Bug ID already exists.")
        self.bugs[bug_id] = Bug(bug_id, title, description)
        return True

    def get_bug(self, bug_id):
        return self.bugs.get(bug_id, None)

    def resolve_bug(self, bug_id):
        bug = self.get_bug(bug_id)
        if not bug:
            raise ValueError("Bug not found.")
        bug.resolve()
        return True

    def list_bugs(self):
        return list(self.bugs.values())


# ===============================
# Unit Tests for Acceptance Testing (Alpha Testing)
# ===============================

class TestBugReportingSystem(unittest.TestCase):
    def setUp(self):
        self.system = BugReportingSystem()

    def test_add_bug(self):
        """Test if a bug can be added successfully."""
        result = self.system.add_bug(1, "Login Error", "App crashes on login")
        self.assertTrue(result)
        self.assertEqual(len(self.system.bugs), 1)

    def test_duplicate_bug_id(self):
        """Test that duplicate bug IDs are not allowed."""
        self.system.add_bug(1, "Login Error", "App crashes on login")
        with self.assertRaises(ValueError):
            self.system.add_bug(1, "UI Issue", "Button misaligned")

    def test_resolve_bug(self):
        """Test if a bug can be resolved successfully."""
        self.system.add_bug(2, "Slow Performance", "App takes time to load")
        self.system.resolve_bug(2)
        bug = self.system.get_bug(2)
        self.assertEqual(bug.status, "Resolved")

    def test_get_nonexistent_bug(self):
        """Test fetching a non-existing bug."""
        bug = self.system.get_bug(99)
        self.assertIsNone(bug)

    def test_list_bugs(self):
        """Test listing all bugs."""
        self.system.add_bug(1, "Crash", "App crash on start")
        self.system.add_bug(2, "UI Issue", "Button color mismatch")
        bugs = self.system.list_bugs()
        self.assertEqual(len(bugs), 2)


# ===============================
# Run Unit Tests (Alpha Testing Simulation)
# ===============================
if __name__ == '__main__':
    unittest.main()

# ============================================
# Alpha Testing - Feature Flag System
# ============================================

import unittest

class FeatureFlagSystem:
    """System to manage feature flags for alpha testers."""
    
    def __init__(self):
        # Stores features and whether they are enabled (True) or disabled (False)
        self.features = {}
        # Optional: map users to features if testing user-based rollout
        self.user_features = {}

    def add_feature(self, feature_name):
        """Add a new feature (disabled by default)."""
        if feature_name in self.features:
            raise ValueError("Feature already exists.")
        self.features[feature_name] = False
        return True

    def enable_feature(self, feature_name):
        """Enable a feature globally."""
        if feature_name not in self.features:
            raise ValueError("Feature not found.")
        self.features[feature_name] = True
        return True

    def disable_feature(self, feature_name):
        """Disable a feature globally."""
        if feature_name not in self.features:
            raise ValueError("Feature not found.")
        self.features[feature_name] = False
        return True

    def is_feature_enabled(self, feature_name):
        """Check if a feature is currently enabled."""
        return self.features.get(feature_name, False)

    def assign_feature_to_user(self, user, feature_name):
        """Assign a specific feature to an alpha tester."""
        if feature_name not in self.features:
            raise ValueError("Feature not found.")
        if user not in self.user_features:
            self.user_features[user] = []
        self.user_features[user].append(feature_name)
        return True

    def is_feature_enabled_for_user(self, user, feature_name):
        """Check if a feature is enabled for a specific user."""
        # Feature must be globally enabled AND assigned to user
        return (
            self.features.get(feature_name, False) and
            feature_name in self.user_features.get(user, [])
        )


# ============================================
# Unit Tests for Feature Flag System (Alpha Testing)
# ============================================

class TestFeatureFlagSystem(unittest.TestCase):

    def setUp(self):
        self.system = FeatureFlagSystem()

    def test_add_feature(self):
        """Test that a new feature can be added."""
        result = self.system.add_feature("DarkMode")
        self.assertTrue(result)
        self.assertIn("DarkMode", self.system.features)

    def test_enable_disable_feature(self):
        """Test enabling and disabling a feature."""
        self.system.add_feature("SearchV2")
        self.system.enable_feature("SearchV2")
        self.assertTrue(self.system.is_feature_enabled("SearchV2"))

        self.system.disable_feature("SearchV2")
        self.assertFalse(self.system.is_feature_enabled("SearchV2"))

    def test_duplicate_feature_addition(self):
        """Test that duplicate features cannot be added."""
        self.system.add_feature("ChatBot")
        with self.assertRaises(ValueError):
            self.system.add_feature("ChatBot")

    def test_assign_feature_to_user(self):
        """Test assigning a feature to a user."""
        self.system.add_feature("BetaDashboard")
        self.system.enable_feature("BetaDashboard")
        self.system.assign_feature_to_user("tester1", "BetaDashboard")

        result = self.system.is_feature_enabled_for_user("tester1", "BetaDashboard")
        self.assertTrue(result)

    def test_feature_not_enabled_globally(self):
        """Test user cannot access feature if globally disabled."""
        self.system.add_feature("VoiceCommand")
        self.system.assign_feature_to_user("tester2", "VoiceCommand")
        result = self.system.is_feature_enabled_for_user("tester2", "VoiceCommand")
        self.assertFalse(result)


# ============================================
# Run Unit Tests (Simulating Alpha Testing)
# ============================================

if __name__ == "__main__":
    unittest.main()

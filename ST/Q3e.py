import unittest

# -------------------------------
# Inventory Module
# -------------------------------
class Inventory:
    def __init__(self):
        # Product name -> quantity
        self.products = {
            "Laptop": 5,
            "Phone": 10,
            "Headphones": 15
        }

    def check_stock(self, product, quantity):
        return self.products.get(product, 0) >= quantity

    def reduce_stock(self, product, quantity):
        if self.check_stock(product, quantity):
            self.products[product] -= quantity
            return True
        return False

# -------------------------------
# Cart Module
# -------------------------------
class Cart:
    def __init__(self, inventory):
        self.inventory = inventory
        self.items = {}  # Product -> quantity

    def add_item(self, product, quantity):
        if self.inventory.check_stock(product, quantity):
            self.items[product] = self.items.get(product, 0) + quantity
            return True
        return False

    def checkout(self):
        for product, qty in self.items.items():
            if not self.inventory.reduce_stock(product, qty):
                raise ValueError(f"Not enough stock for {product}")
        total_items = sum(self.items.values())
        self.items = {}  # Clear cart after checkout
        return total_items

# -------------------------------
# Payment Module
# -------------------------------
class Payment:
    def process_payment(self, amount):
        # Simplified: always succeed if amount > 0
        if amount <= 0:
            raise ValueError("Invalid payment amount")
        return True

# -------------------------------
# Unit Tests for E-Commerce System
# -------------------------------
class TestECommerceSystem(unittest.TestCase):

    def setUp(self):
        self.inventory = Inventory()
        self.cart = Cart(self.inventory)
        self.payment = Payment()

    def test_add_to_cart_and_checkout(self):
        # Add items
        self.assertTrue(self.cart.add_item("Laptop", 2))
        self.assertTrue(self.cart.add_item("Phone", 3))
        # Checkout updates inventory
        total_items = self.cart.checkout()
        self.assertEqual(total_items, 5)
        # Inventory updated
        self.assertEqual(self.inventory.products["Laptop"], 3)
        self.assertEqual(self.inventory.products["Phone"], 7)

    def test_checkout_not_enough_stock(self):
        # Add more than available stock
        self.assertFalse(self.cart.add_item("Laptop", 10))
        # Add valid quantity
        self.assertTrue(self.cart.add_item("Laptop", 2))
        # Reduce inventory manually to simulate stock issue
        self.inventory.products["Laptop"] = 1
        with self.assertRaises(ValueError):
            self.cart.checkout()

    def test_payment_processing(self):
        # Process valid payment
        self.assertTrue(self.payment.process_payment(100))
        # Process invalid payment
        with self.assertRaises(ValueError):
            self.payment.process_payment(0)

# -------------------------------
# Run Unit Tests
# -------------------------------
if __name__ == "__main__":
    unittest.main()

import unittest
import sqlite3

# -------------------------------
# In-Memory Database CRUD System
# -------------------------------
class DatabaseCRUD:
    def __init__(self):
        # Use in-memory SQLite database
        self.conn = sqlite3.connect(":memory:")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        ''')
        self.conn.commit()

    def create_user(self, name, age):
        self.cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        self.conn.commit()
        return self.cursor.lastrowid

    def read_user(self, user_id):
        self.cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        return self.cursor.fetchone()

    def update_user(self, user_id, name, age):
        self.cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        self.cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

# -------------------------------
# Unit Tests
# -------------------------------
class TestDatabaseCRUD(unittest.TestCase):

    def setUp(self):
        self.db = DatabaseCRUD()  # New in-memory DB for each test

    def tearDown(self):
        self.db.close()

    def test_create_and_read_user(self):
        user_id = self.db.create_user("Alice", 25)
        user = self.db.read_user(user_id)
        self.assertEqual(user[1], "Alice")
        self.assertEqual(user[2], 25)

    def test_update_user(self):
        user_id = self.db.create_user("Bob", 30)
        self.db.update_user(user_id, "Bobby", 35)
        user = self.db.read_user(user_id)
        self.assertEqual(user[1], "Bobby")
        self.assertEqual(user[2], 35)

    def test_delete_user(self):
        user_id = self.db.create_user("Charlie", 40)
        self.db.delete_user(user_id)
        user = self.db.read_user(user_id)
        self.assertIsNone(user)

# -------------------------------
# Run Unit Tests
# -------------------------------
if __name__ == "__main__":
    unittest.main()

import json
from pathlib import Path


class Auth:
    def __init__(self):
        self.users_file = Path(__file__).parent / "users.json"
        self.users = self.load_users()

    def load_users(self):
        """Load users from JSON file with error handling"""
        try:
            if self.users_file.exists():
                with open(self.users_file, 'r') as f:
                    content = f.read().strip()
                    if content:
                        return json.loads(content)
                    else:
                        return {}
            return {}
        except (json.JSONDecodeError, FileNotFoundError):
            print("Warning: users.json was corrupted. Creating new file.")
            return {}

    def save_users(self):
        """Save users to JSON file"""
        try:
            with open(self.users_file, 'w') as f:
                json.dump(self.users, f, indent=2)
        except Exception as e:
            print(f"Error saving users: {e}")

    def register(self, name, email, password):
        """Register a new user"""
        if email in self.users:
            return False, "Email already registered!"

        self.users[email] = {
            "name": name,
            "email": email,
            "password": password
        }
        self.save_users()
        return True, "Registration successful!"

    def login(self, email, password):
        """Login user"""
        if email not in self.users:
            return False, "User not found!", None

        user = self.users[email]
        if user["password"] != password:
            return False, "Invalid password!", None

        return True, "Login successful!", user["name"]
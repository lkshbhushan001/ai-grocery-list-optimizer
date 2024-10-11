from config import db

class User:
    def __init__(self, name, preferences, dietary_restrictions):
        self.name = name
        self.preferences = preferences
        self.dietary_restrictions = dietary_restrictions

    def save_to_db(self):
        # Insert user data into MongoDB
        db.users.insert_one({
            'name': self.name,
            'preferences': self.preferences,
            'dietary_restrictions': self.dietary_restrictions
        })


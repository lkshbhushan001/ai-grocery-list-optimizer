from config import db

class User:
    def __init__(self, name, preferences, dietary_restrictions):
        self.name = name
        self.preferences = preferences
        self.dietary_restrictions = dietary_restrictions

    def save(self):
        db.users.insert_one({
            'name': self.name,
            'preferences': self.preferences,
            'dietary_restrictions': self.dietary_restrictions
        })

    @staticmethod
    def get_user_by_name(name):
        return db.users.find_one({'name': name})


class User:
    def __init__(self, name, preferences, dietary_restrictions, past_purchases=None):
        self.name = name
        self.preferences = preferences
        self.dietary_restrictions = dietary_restrictions
        self.past_purchases = past_purchases or []

    def save(self):
        db.users.insert_one({
            'name': self.name,
            'preferences': self.preferences,
            'dietary_restrictions': self.dietary_restrictions,
            'past_purchases': self.past_purchases
        })

    @staticmethod
    def get_user_by_name(name):
        return db.users.find_one({'name': name})

    @staticmethod
    def update_purchases(user_id, new_purchases):
        db.users.update_one(
            {'_id': user_id},
            {'$push': {'past_purchases': {'$each': new_purchases}}}
        )

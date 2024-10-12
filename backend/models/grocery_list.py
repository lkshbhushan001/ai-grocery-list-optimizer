from config import db

class GroceryList:
    def __init__(self, user_id, items):
        self.user_id = user_id
        self.items = items

    def save(self):
        db.grocery_lists.insert_one({
            'user_id': self.user_id,
            'items': self.items
        })

    @staticmethod
    def get_list_by_user(user_id):
        return db.grocery_lists.find_one({'user_id': user_id})

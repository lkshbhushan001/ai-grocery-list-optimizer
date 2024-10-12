# models/shopping_list.py
from pymongo import MongoClient
from config import Config

# Initialize MongoDB Client
client = MongoClient(Config.MONGO_URI)
db = client.Cluster0  

class ShoppingList:
    def __init__(self, name, items):
        self.name = name
        self.items = items

    @staticmethod
    def create_shopping_list(data):
        shopping_lists_collection = db.shopping_lists  # Collection name
        result = shopping_lists_collection.insert_one(data)
        return str(result.inserted_id)

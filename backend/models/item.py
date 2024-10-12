# models/item.py
from pymongo import MongoClient
from config import Config

# Initialize MongoDB Client
client = MongoClient(Config.MONGO_URI)
db = client.Cluster0  # Replace with your database name

class Item:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    @staticmethod
    def create_item(data):
        items_collection = db.items  # Collection name
        result = items_collection.insert_one(data)
        return str(result.inserted_id)

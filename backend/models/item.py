# models/item.py
from pymongo import MongoClient
from config import Config

# Initialize MongoDB Client
client = MongoClient(Config.MONGO_URI)
db = client.grocery_optimization  # Replace with your database name

class Item:
    @staticmethod
    def get_all_items():
        return list(db.items.find())

    @staticmethod
    def create_item(data):
        item = {
            "name": data["name"],
            "quantity": data["quantity"],
            "expiry_date": data["expiry_date"],
            "usage_rate": data["usage_rate"]  # usage per day or week
        }
        db.items.insert_one(item)
        return item
    
    @staticmethod
    def delete_item(data):
        item = {
            "name": data["name"],
            "quantity": data["quantity"],
            "expiry_date": data["expiry_date"],
            "usage_rate": data["usage_rate"]  # usage per day or week
        }
        db.items.delete_one(item)
        return item
    
    @staticmethod
    def delete_item(data):
        item = {
            "name": data["name"],
            "quantity": data["quantity"],
            "expiry_date": data["expiry_date"],
            "usage_rate": data["usage_rate"] 
        }
        db.items.delete_one(item)
        return item
    
    @staticmethod
    def update_item(data):
        item = {
            "name": data["name"],
            "quantity": data["quantity"],
            "expiry_date": data["expiry_date"],
            "usage_rate": data["usage_rate"]  
        }
        db.items.update_one(item)
        return item
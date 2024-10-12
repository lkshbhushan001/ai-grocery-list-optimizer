from pymongo import MongoClient

# MongoDB connection setup
client = MongoClient('mongodb+srv://lkshbhushan001:<Offstamp@123>@cluster0.ao6qi.mongodb.net/')  # Update with MongoDB URI
db = client['grocery_optimizer']  # Database name

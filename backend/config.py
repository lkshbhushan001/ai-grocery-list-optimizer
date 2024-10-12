# backend/config.py

from urllib.parse import quote_plus
from pymongo import MongoClient

# Your actual MongoDB credentials
username = 'lkshbhushan001' 
password = '<Offstamp@123>'  

# Encode the username and password
encoded_username = quote_plus(username)
encoded_password = quote_plus(password)

# Update the MongoDB URI with encoded credentials
client = MongoClient(f'mongodb+srv://{encoded_username}:{encoded_password}@cluster0.ao6qi.mongodb.net/' )

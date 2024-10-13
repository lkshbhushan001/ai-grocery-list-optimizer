from flask import Flask
from flask_cors import CORS
from config.settings import Config
from api.routes import api
from models import Item, shoppinglist
from pymongo import MongoClient


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)  # Enable CORS
# Load configuration
app.config.from_object(Config)

# Initialize MongoDB Client
client = MongoClient(Config.MONGO_URI)
db = client.grocery_optimization 

# Import routes
from api.routes import api
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)

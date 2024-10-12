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
db = client.Cluster0  # Replace with your actual database name

# Register API Blueprint
app.register_blueprint(api)

# Define a basic route for testing
@app.route('/')
def home():
    return "Welcome to the AI-Based Grocery Shopping List Optimizer!"

# Error handling
@app.errorhandler(404)
def not_found(error):
    return {"message": "Not found"}, 404

@app.errorhandler(500)
def internal_error(error):
    return {"message": "Internal Server Error"}, 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)

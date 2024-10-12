from flask import Flask, request, jsonify
from models.user import User
from routes.user_routes import user_blueprint
from routes.grocery_routes import grocery_blueprint
from config import db

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Grocery Shopping List Optimizer!"

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)

@app.route('/user/preferences', methods=['POST'])
def save_preferences():
    data = request.get_json()
    user = User(
        name=data['name'],
        preferences=data['preferences'],
        dietary_restrictions=data['dietary_restrictions']
    )
    user.save_to_db()
    return jsonify({"message": "User preferences saved"}), 201


app = Flask(__name__)

# Registering Blueprints (Modular Routes)
app.register_blueprint(user_blueprint)
app.register_blueprint(grocery_blueprint)

if __name__ == "__main__":
    app.run(debug=True)



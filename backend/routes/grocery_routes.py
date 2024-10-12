from flask import Blueprint, jsonify, request
from services.grocery_optimizer import generate_grocery_list
from models.grocery_list import GroceryList
from models.user import User

grocery_blueprint = Blueprint('grocery_blueprint', __name__)

@grocery_blueprint.route('/grocery-list', methods=['POST'])
def create_grocery_list():
    data = request.get_json()
    user = User.get_user_by_name(data['name'])

    if not user:
        return jsonify({"message": "User not found"}), 404

    grocery_list = generate_grocery_list(user['preferences'], user['dietary_restrictions'])
    
    # Save the generated list
    grocery = GroceryList(user_id=user['_id'], items=grocery_list)
    grocery.save()

    return jsonify({"grocery_list": grocery_list}), 200




from flask import Blueprint, request, jsonify
from models.user import User

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/user/preferences', methods=['POST'])
def save_preferences():
    data = request.get_json()
    user = User(
        name=data['name'],
        preferences=data['preferences'],
        dietary_restrictions=data['dietary_restrictions']
    )
    user.save()
    return jsonify({"message": "User preferences saved"}), 201

@user_blueprint.route('/user/<name>', methods=['GET'])
def get_user(name):
    user = User.get_user_by_name(name)
    if user:
        return jsonify(user), 200
    return jsonify({"message": "User not found"}), 404

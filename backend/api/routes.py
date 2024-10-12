from flask import jsonify, request, Blueprint
from .views import get_items, add_item, get_shopping_list
from models import Item


api = Blueprint('api', __name__)

@api.route('/items', methods=['POST'])
def add_item():
    data = request.json
    item_id = Item.create_item(data)
    return jsonify({"item_id": item_id}), 201

@api.route('/items', methods=['GET'])
def get_items():
    items = Item.get_items()
    return jsonify(items), 200

@api.route('/items/<item_id>', methods=['GET'])
def get_item(item_id):
    item = Item.get_item(item_id)
    return jsonify(item), 200 if item else 404

@api.route('/items/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    Item.update_item(item_id, data)
    return jsonify({"message": "Item updated"}), 200

@api.route('/items/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    Item.delete_item(item_id)
    return jsonify({"message": "Item deleted"}), 204


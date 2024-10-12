from flask import jsonify
from models import Item, shoppinglist

def get_items():
    items = Item.query.all()
    return jsonify([item.to_dict() for item in items])

def add_item(data):
    new_item = Item(name=data['name'], quantity=data['quantity'])
    shoppinglist.db.session.add(new_item)
    shoppinglist.db.session.commit()
    return jsonify(new_item.to_dict()), 201

def get_shopping_list():
    # Logic for generating the shopping list based on AI model or preferences
    # For now, we can return all items as the shopping list
    items = Item.query.all()
    shopping_list = [item.to_dict() for item in items]
    return jsonify(shopping_list)

def update_item(item_id, data):
    item = Item.query.get(item_id)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    item.name = data['name']
    item.quantity = data['quantity']
    shoppinglist.db.session.commit()
    return jsonify(item.to_dict())

def delete_item(item_id):
    item = Item.query.get(item_id)
    if item is None:
        return jsonify({'message': 'Item not found'}), 404
    shoppinglist.db.session.delete(item)
    shoppinglist.db.session.commit()
    return jsonify({'message': 'Item deleted successfully'})

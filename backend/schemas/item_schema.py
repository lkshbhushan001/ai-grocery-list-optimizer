from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    quantity = fields.Int(required=True)
    expiry_date = fields.Date(required=True)
    usage_rate = fields.Float(required=True)

item_schema = ItemSchema()

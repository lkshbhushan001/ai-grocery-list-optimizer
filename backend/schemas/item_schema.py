from marshmallow import Schema, fields

class ItemSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    quantity = fields.Int()

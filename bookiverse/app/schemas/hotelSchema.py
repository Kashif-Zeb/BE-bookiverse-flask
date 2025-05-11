from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
    post_dump
)

class hotelSchema(Schema):
    hotel_id = fields.Integer(dump_only=True)
    hotel_name = fields.String(required=True)
    hotel_rooms = fields.String(required=True)
    price = fields.Integer(required=True,attribute ='hotel_price')
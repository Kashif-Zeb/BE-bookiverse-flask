from marshmallow import (
    Schema,
    ValidationError,
    fields,
    validate,
    validates,
    post_dump
)

class FlightSchema(Schema):
    flight_id = fields.Integer(dump_only=True)
    flight_name = fields.String(required=True)
    plane_name = fields.String(required=True)
    flight_origin =fields.String(required=True)
    flight_departure =fields.String(required=True)
    flight_date = fields.DateTime(format="%Y-%m-%d %H:%M:%S")
    flight_price = fields.Integer(required=True)
    company = fields.String(required=True)
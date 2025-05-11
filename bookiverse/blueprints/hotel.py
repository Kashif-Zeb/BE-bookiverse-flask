from encodings.punycode import T
import http
import re
from flask import Flask,Blueprint, jsonify
from webargs.flaskparser import use_args
from bookiverse.app.schemas import flightSchema
from bookiverse.app.schemas.hotelSchema import hotelSchema
from bookiverse.app.bl.hotelBLC import hotelBLC
from http import HTTPStatus
from flask_jwt_extended import jwt_required
bp = Blueprint('hotel',__name__)

@bp.route('/hotel',methods=["POST"])
# @jwt_required()
@use_args(hotelSchema,location='json')
def hotel_flight(args):
    try:
        flight = hotelBLC.Inserting_the_hotel_data_into_db(args)
        schema = hotelSchema()
        result = schema.dump(flight)
        return jsonify(result),HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY
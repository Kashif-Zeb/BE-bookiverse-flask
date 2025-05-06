from encodings.punycode import T
import http
import re
from flask import Flask,Blueprint, jsonify
from pydash import result
from webargs.flaskparser import use_args
from bookiverse.app.schemas import flightSchema
from bookiverse.app.schemas.flightSchema import FlightSchema
from bookiverse.app.bl.flightBLC import FlightBLC
from http import HTTPStatus
from flask_jwt_extended import jwt_required
bp = Blueprint('flight',__name__)

@bp.route('/add-flight',methods=["POST"])
@jwt_required()
@use_args(FlightSchema,location='json')
def insert_flight(args):
    try:
        flight = FlightBLC.Inserting_the_flight_data_into_db(args)
        schema = FlightSchema()
        result = schema.dump(flight)
        return jsonify(result),HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


@bp.route("/get-all-flights",methods=["GET"])
@jwt_required()
def get_all_flights():
    try:
        flights = FlightBLC.geting_all_flights_from_db()
        schema = FlightSchema(many=True)
        result = schema.dump(flights)
        return jsonify(result),HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

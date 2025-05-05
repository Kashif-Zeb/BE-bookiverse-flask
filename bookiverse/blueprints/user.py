import json
from flask import request, jsonify,after_this_request,g
from webargs.flaskparser import use_args
from functools import wraps
from flask import Blueprint
from marshmallow import fields,validate
from bookiverse.app.schemas.userSchema import user_dump, userSchema
from bookiverse.app.db import db
from bookiverse.app.repositories.userRepository import userRepository
from bookiverse.app.bl.userBLC import userBLC
from http import HTTPStatus
from flask_jwt_extended import jwt_required,JWTManager,decode_token,get_jwt_identity,create_access_token
from functools import wraps
from bookiverse.tasks import file
from bookiverse.signals import user_logged_in
from bookiverse.limiters import limiter,cache

bp = Blueprint("user", __name__)



@bp.route("/register",methods=["POST"])
@use_args(userSchema,location="json")
def register(args:dict):
    try:
        user =userBLC.adding_user_details(args)
        return jsonify({"message":"you registered successfully"}),HTTPStatus.CREATED
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route("/login",methods=["POST"])
@use_args({"email":fields.Email(required=True),
           "password":fields.String(required=True)},location="json")
def login(args):
    try:
        access_token,refresh_token,user =userBLC.checking_user(args)
        schema = user_dump()
        user = schema.dump(user)
        return jsonify({"access_token":access_token,"refresh_token":refresh_token,"user_details":user}),HTTPStatus.OK
    except Exception as e:
        return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

@bp.route('/refresh', methods=['POST'])
@jwt_required(refresh=True)  # Only accepts refresh tokens
def refresh():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify({
        'access_token': new_access_token
    }), 200

# @bp.route("/add_employee",methods=["POST"])
# @use_args(employeeSchema,location="json")
# def add_employee(args:dict):
#     try:
#         employee = employeeBLC.adding_employee(args)
#         schema = employeeSchema()
#         res = schema.dump(employee)
#         return res,HTTPStatus.OK
#     except Exception as e:
#         return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY



# @bp.route("/get_employee_by_id",methods=["GET"])
# @jwt_required()
# # @limiter.limit("2 per minute")
# # @limiter.limit(get_user_rate)
# # @cache.cached(timeout=150)
# @use_args({"employee_id":fields.Integer(required=True,validate=validate.Range(min=1,error="employee_id must be a positive integer"))},location="query")
# def get_employee_by_id(args):
#     # try:
#         employee = employeeBLC.getting_employee(args)
#         schema = employee_details_with_DJ()
#         res = schema.dump(employee)
#         file.delay(res)
#         return res,HTTPStatus.OK
#     # except Exception as e:
#     #     return jsonify({"message":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


# @bp.route("/get_all_employee",methods=["GET"])
# # @jwt_required()
# @use_args({"page":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer")),
#            "per_page":fields.Integer(required=True,validate=validate.Range(min=1,error="per_page must be a positive integer"))},location="query")
# def get_all_employee(args:dict):
#     try:
#         employess = employeeBLC.getting_all_employee(args)
#         get_emp = employess["employees"]
#         schema = employee_details_with_DJ(many=True)
#         res = schema.dump(get_emp)
#         response = {
#             'employees': res,
#             'page': employess['page'],
#             'per_page': employess['per_page'],
#             'total': employess['total'],
#             'pages': employess['pages'],
#             'has_next': employess['has_next'],
#             'has_prev': employess['has_prev']
#         }
#         return response,HTTPStatus.OK
#     except Exception as e:
#         return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY


# @bp.route("/update_employee",methods=["PUT"])
# @use_args(update_employee,location="json")
# def updateing_employee(args:dict):
#     try:
#         updating_employee =employeeBLC.updating_employee(args)
#         schema = update_employee()
#         res = schema.dump(updating_employee)
#         return res,HTTPStatus.OK
#     except Exception as e:
#         return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY

# @bp.route("/delete_employee",methods=["DELETE"])
# @use_args({"id":fields.Integer(required=True,validate=validate.Range(min=1,error="page must be a positive integer"))},location="query")
# def delete_employee(args:dict):
#     try:
#         employee_deleted = employeeBLC.deleting_employee(args)
#         return jsonify({"message":employee_deleted}),HTTPStatus.OK
#     except Exception as e:
#         return jsonify({"error":str(e)}),HTTPStatus.UNPROCESSABLE_ENTITY
# @bp.route("/get_employee_with_path",methods=["GET"])
# @use_args({"employee_id":fields.Integer()},location="query")
# def getting_employee_with(args):
#     with_path  = employeeBLC.get_employee_with_path(args)
#     schema = hybrid(many=True)
#     # serialized_data = [schema.serialize(item) for item in with_path]
#     res = schema.dump(with_path)
#     return jsonify(res)

# # dynamic_schema = dynamic()
# @bp.route("/checkruntimeschema",methods=["POST"])
# # @use_args(dynamic_schema,location="json")
# def checkruntimeschema():
#     data_khan = request.json
#     title = data_khan.get("title")
#     if title=="esg":
#         esg =ESGSchema()
#         data_khan = esg.load(data_khan)
#     else:
#         auto = AutoSchema()
#         data_khan = auto.load(data_khan)


#     return jsonify(data_khan)


# @bp.route("/validation_on_file",methods=["POST"])
# @use_args(file_validation,location="json")
# def file_valid(args):
#     return jsonify(args)

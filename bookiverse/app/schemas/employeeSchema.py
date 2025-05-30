# import re
# from marshmallow import (
#     Schema,
#     ValidationError,
#     fields,
#     validate,
#     validates,
#     post_dump, validates_schema,ValidationError,pre_load
# )
# import pandas as pd


# def no_space_validation(name):
#     def validator(value):
#         if value.startswith(" "):
#             raise ValidationError(f"{name} cannot start with whitespaces")
#         if value.endswith(" "):
#             raise ValidationError(f"{name} cannot end with whitespaces")
#     return validator

# def phone(key):
#     def validator(value:str):
#         if not value.isdigit():
#             raise ValidationError(f"{key} must be a positive integer")
#     return validator
# def check_not_float(key):
#     def validator(value):
#         if not isinstance(value,int):
#             raise ValidationError(f"{key} must be a integer")
#     return validator
# class employeeSchema(Schema):
#     id = fields.Integer(dump_only=True)
#     name = fields.String(required=True,validate=[validate.Length(min=1,error="employee name cannot be left empty"),no_space_validation("name")])
#     address = fields.String(validate=no_space_validation("address"))
#     phone = fields.String(required=True,validate=[validate.Length(min=6,max=20,error="phone number must be between 6 to 20 digits"),phone("phone")])
#     email = fields.Email(required=True)
#     job_id = fields.Integer(required=True,validate=[validate.Range(min=1,error="job_id must be a positive integer"),check_not_float("job_id")])
#     department_id = fields.Integer(required=True,validate=validate.Range(min=1,error="department_id must be a positive integer"))

# # class path(Schema):
# #     id = fields.Integer()
# #     path_name = fields.String()

# # class mm(Schema):
# #     document_count = fields.Integer(attribute = "document_count")
# #     @staticmethod
# #     def serialize(employee_with_count):
# #         # employee_with_count is expected to be a tuple (<Employee instance>, count)
# #         employee, count = employee_with_count
# #         return {
# #             'employee': employee_khan().dump(employee),
# #             'document_count': count
# #         }
# # class employee_khan(employeeSchema):
# #     comming_path = fields.Nested(path, allow_none=True)
# #     going_path = fields.Nested(path, allow_none=True)
# #     # @staticmethod
# #     # def serialize(employee_with_count):
# #     #     # employee_with_count is expected to be a tuple (<Employee instance>, count)
# #     #     employee, count = employee_with_count
# #     #     return {
# #     #         'employee': employeeSchema().dump(employee),
# #     #         'document_count': count
# #         # }
# #     # department = fields.Nested(DepartmentSchema)  # Assuming you have a DepartmentSchema
# #     # documents = fields.List(fields.Nested(documentSchema), allow_none=True)
# # class hybrid(employeeSchema):
# #     coming_path = fields.Nested(path, allow_none=True)
# #     going_path = fields.Nested(path, allow_none=True)
# #     document_count = fields.Integer()
# # class employee_path(Schema):
# #     id  = fields.Integer(attribute = 'id')
# #     going_path_id = fields.Integer(attribute='going_path.id')
# #     going_path_name = fields.String(attribute='going_path.path_name')
# #     comming_path_id = fields.Integer(attribute='coming_path.id',allow_none=True)
# #     comming_path_name = fields.String(attribute='coming_path.path_name',allow_none=True)

# # class update_employee(employeeSchema):
# #     id = fields.Integer(required=True,validate=validate.Range(min=1,error="id must be a positive integer"))

# # class employee_details_with_DJ(employeeSchema):
# #     jobs = fields.Nested(JobSchema, exclude=("job_id",))
# #     department = fields.Nested(DepartmentSchema, exclude=("department_id",))

# #     @post_dump
# #     def remove_id(self,data,**kwargs):
# #         data.pop("job_id",None)
# #         data.pop("department_id",None)
# #         return data


# # class ESGSchema(Schema):
# #     title = fields.Str(required=True)
# #     esg_field = fields.Str(required=True)  

# # class AutoSchema(Schema):
# #     title = fields.Str(required=True)
# #     auto_field = fields.Int(required=True)


# # def validation_on_file(file):
# #     file_type = file.split(".")[-1]
# #     if file_type!="tsv":
# #         raise ValidationError("it support only tsv file only")
    
# #     data = pd.read_table(file, header=None, names=['values'])
# #     if len(data)< 9:
# #         raise ValidationError("in importer flow imei should be pass in file more than or equal to 10")
# #     # pattern = r'^[a-zA-Z0-9\x2d]{10,20}$'
# #     imei = [str(i) for i in data["values"]]
# #     valid = []
# #     for i in imei:
# #         if len(i)>14 and len(i) < 16:
# #             valid.append(i)
# #         else:
# #             raise ValidationError("IMEI is invalid or length is invalid")
# #     # data["35192705700220"]
# #     return file
# # class file_validation(Schema):
# #     file = fields.String(required=True)

# #     @pre_load
# #     def validation(self,data,**kwargs):
# #         print(kwargs,data)
# #         if "file" in data:
# #             file = data["file"]
# #             valid = validation_on_file(file)
# #         else:
# #             raise ValidationError("plz provide the file")
# #         return valid


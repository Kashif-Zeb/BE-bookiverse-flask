# from sqlalchemy import func
from sqlalchemy import func
from bookiverse.app.models.users import Users
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError

class userRepository:
    # @staticmethod
    # def add_employee_in_db(session:scoped_session,args:dict) -> Employee:
    #     try:
    #         employee = Employee(**args)
    #         session.add(employee)
    #         session.flush()
    #         return employee
    #     except SQLAlchemyError:
    #         session.rollback()
    #         raise

    
    # @staticmethod
    # def get_employee_by_id_for_all_details(session:scoped_session,args:dict) -> Employee:
    #     try:
    #         res =session.query(Employee).\
    #             filter(Employee.id == args.get("employee_id")).\
    #             options(joinedload(Employee.jobs), joinedload(Employee.department)).first()
    #         # res = session.query(Employee).\
    #         #         join(Job, Employee.job_id == Job.job_id).\
    #         #         join(Department, Employee.department_id == Department.department_id).\
    #         #         filter(Employee.id == args.get("employee_id")).\
    #         #         first()
    #         return res
    #     except SQLAlchemyError:
    #         raise

    
    # @staticmethod
    # def get_all_employee_from_db(session:scoped_session,args:dict) -> Job:
    #     try:
    #         offset = (args.get("page") - 1) * args.get("per_page")
    #         res = session.query(Employee).\
    #         options(joinedload(Employee.jobs),joinedload(Employee.department))
    #         employees = res.offset(offset).limit(args.get("per_page")).all()
        
    #         # Get total count for pagination metadata
    #         total = res.count()
    #         return res,total
    #     except SQLAlchemyError:
    #         raise

    # @staticmethod
    # def get_employee_by_id(session:scoped_session,args:dict):
    #     try:
    #         res = session.query(Employee).filter(Employee.id==args.get("id")).first()
    #         return res
    #     except SQLAlchemyError:
    #         raise
    # @staticmethod
    # def get_employee_by_id2(session:scoped_session,args:dict):
    #     try:
    #         res = session.query(Employee).filter(Employee.id==args.get("employee_id")).first()
    #         return res
    #     except SQLAlchemyError:
    #         raise
    # @staticmethod
    # def update_employee_in_db(session:scoped_session,check_employee:Employee,args:dict):
    #     try:
    #         check_employee.name = args.get("name")
    #         check_employee.email = args.get("email")
    #         check_employee.address = args.get("address")
    #         check_employee.job_id = args.get("job_id")
    #         check_employee.department_id = args.get("department_id")
    #         check_employee.phone  =args.get("phone")
    #         session.flush()

    #     except SQLAlchemyError:
    #         raise
    

    @staticmethod
    def save_user_details_in_db(session:scoped_session,args:dict):
        try:
            password = args.pop("hash_password")
            user = Users(**args)
            user.set_password(password)
            session.add(user)
            session.flush()
            return user
        except SQLAlchemyError:
            raise
    

    @staticmethod
    def get_user(session:scoped_session,args:dict):
        try:
            res = session.query(Users).filter(Users.email==args.get("email")).first()
            return res
        except SQLAlchemyError:
            raise

#     @staticmethod
#     def get_employee_with_path_from_db(session:scoped_session,args:dict):
#         employee_id = args.get("employee_id")
#         document_count_subquery = (
#             session.query(
#                 Document.employee_id,
#                 func.count(Document.document_id).label('document_count')
#             )
#             .group_by(Document.employee_id)
#             .subquery()
#         )
#         res = session.query(Employee).options(
#             joinedload(Employee.going_path),
#             joinedload(Employee.coming_path),
#         ).all() #.outerjoin(document_count_subquery, Employee.id == document_count_subquery.c.employee_id).add_columns(document_count_subquery.c.document_count).all()
# #         employee_with_document_count = [
# #     (employee, document_count if document_count else 0)
# #     for employee, document_count in res
# # ]
#         return res

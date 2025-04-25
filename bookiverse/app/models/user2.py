# from hr.app.db import db
# from sqlalchemy import Integer ,String,Column
# from werkzeug.security import generate_password_hash,check_password_hash
# user_mobile = db.Table("user_mobile",db.Column("user_id",db.Integer,db.ForeignKey("users2.user_id"),primary_key=True),
#                        db.Column("mobile_id",db.Integer,db.ForeignKey("mobile.id"),primary_key=True),
#                        db.Column("quantity",db.Integer,default=1)
#                        )
# class Users2(db.Model):
#     __tablename__="users2"
#     user_id = Column(Integer,primary_key=True,autoincrement=True)
#     username = Column(String(50),nullable=False,unique=True)
#     mobiles = db.relationship("Mobile",secondary=user_mobile,back_populates="user2s")
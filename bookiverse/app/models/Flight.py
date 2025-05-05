from bookiverse.app.db import db
from sqlalchemy import Integer ,String,Column,DateTime
from datetime import datetime

class Flight(db.Model):
    flight_id = Column(Integer,primary_key=True,autoincrement=True)
    flight_name = Column(String(50),nullable=False)
    plane_name = Column(String(50),nullable=False)
    flight_origin = db.Column(db.String(50),nullable=False)
    flight_departure = Column(String(50),nullable=False)
    flight_date = Column(DateTime,nullable=False,default=datetime.now())
    flight_price = Column(Integer,nullable=False)
    company = Column(String(50),nullable=False)
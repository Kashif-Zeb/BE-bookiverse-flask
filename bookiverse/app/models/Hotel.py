from enum import Enum
from bookiverse.app.db import db
from sqlalchemy import ForeignKey, Integer ,String,Column,ForeignKey,Enum as sqlenum


class Room(Enum):
    Room_1 ='1 room'
    Room_2 ='2 room'
    Room_3 ='3 room'
    Room_4 ='4 room'
    Suite ='suite'  

class Hotel(db.Model):
    __tablename__ = 'hotel'
    hotel_id = Column(Integer,primary_key=True,autoincrement=True)
    hotel_name = Column(String(50),nullable=False)
    hotel_rooms = Column(sqlenum(Room),nullable=False)
    hotel_price = Column(Integer,nullable=False)
import re
from sqlalchemy import func
import sqlalchemy
from bookiverse.app.models.Hotel import Hotel
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError


class hotelRepository:


    @staticmethod
    def save_hotel_in_db(args:dict,session:scoped_session):
        try:
            hotel = Hotel(**args)
            session.add(hotel)
            session.flush()
            return hotel
        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(e)





from flask import session
from bookiverse.app.repositories.hotelRepository import hotelRepository
from bookiverse.app.db import db

class hotelBLC:


    @staticmethod
    def get_session():
        return db.session
    

    @staticmethod
    def Inserting_the_hotel_data_into_db(args:dict):
        session = hotelBLC.get_session()
        hotel = hotelRepository.save_hotel_in_db(args,session)
        if hotel:
            return hotel
        
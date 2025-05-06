from flask import session
from bookiverse.app.repositories import flightRepository
from bookiverse.app.repositories.flightRepository import FlightRepository
# from http import HTTPStatus
from bookiverse.app.db import db

from sqlalchemy.orm import scoped_session

class FlightBLC:

    @staticmethod
    def get_session():
        return db.session
        
    
    @staticmethod
    def Inserting_the_flight_data_into_db(args:dict):
        session:scoped_session  = FlightBLC.get_session()
        flight = FlightRepository.insert_flight_in_db(args,session)
        if flight:
            session.commit()
            return flight
        else:
            raise Exception("flight record not added something went wrong")
    

    @staticmethod
    def geting_all_flights_from_db():
        session = FlightBLC.get_session()
        flights = FlightRepository.get_all_flights_from_db(session)
        if flights:
            return flights
        raise Exception("there is no flights records")
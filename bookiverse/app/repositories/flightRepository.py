from sqlalchemy import func
from bookiverse.app.models.Flight import Flight
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import joinedload
from sqlalchemy.exc import SQLAlchemyError


class FlightRepository:

    @staticmethod
    def insert_flight_in_db(args:dict,session:scoped_session):
        try:
            flight = Flight(**args)
            session.add(flight)
            session.flush()
            return flight
        except SQLAlchemyError as e:
            session.rollback()
            raise Exception(e)
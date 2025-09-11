from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey, Boolean, TIMESTAMP, func
from sqlalchemy.orm import relationship
from db import Base

class Tourist(Base):
    __tablename__ = "tourists"
    id = Column(Integer, primary_key=True, index=True)
    digital_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    passport_or_aadhaar = Column(String, nullable=False)
    phone = Column(String)
    emergency_contact = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())

    trips = relationship("Trip", back_populates="tourist")
    alerts = relationship("Alert", back_populates="tourist")

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True, index=True)
    tourist_id = Column(Integer, ForeignKey("tourists.id"))
    itinerary = Column(Text)
    start_date = Column(Date)
    end_date = Column(Date)
    safety_score = Column(Integer, default=100)
    created_at = Column(TIMESTAMP, server_default=func.now())

    tourist = relationship("Tourist", back_populates="trips")
    alerts = relationship("Alert", back_populates="trip")

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    tourist_id = Column(Integer, ForeignKey("tourists.id"))
    trip_id = Column(Integer, ForeignKey("trips.id"))
    alert_type = Column(String)
    description = Column(Text)
    location = Column(String)
    created_at = Column(TIMESTAMP, server_default=func.now())
    resolved = Column(Boolean, default=False)

    tourist = relationship("Tourist", back_populates="alerts")
    trip = relationship("Trip", back_populates="alerts")

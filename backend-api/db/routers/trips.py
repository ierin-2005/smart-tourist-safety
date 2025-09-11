from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from db import get_db

router = APIRouter(prefix="/trips", tags=["Trips"])

@router.get("/")
def get_trips(db: Session = Depends(get_db)):
    return db.query(models.Trip).all()

@router.post("/")
def add_trip(trip: dict, db: Session = Depends(get_db)):
    new_trip = models.Trip(**trip)
    db.add(new_trip)
    db.commit()
    db.refresh(new_trip)
    return new_trip

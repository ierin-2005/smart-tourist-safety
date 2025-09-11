from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from db import get_db

router = APIRouter(prefix="/tourists", tags=["Tourists"])

@router.get("/")
def get_tourists(db: Session = Depends(get_db)):
    return db.query(models.Tourist).all()

@router.post("/")
def add_tourist(tourist: dict, db: Session = Depends(get_db)):
    new_tourist = models.Tourist(**tourist)
    db.add(new_tourist)
    db.commit()
    db.refresh(new_tourist)
    return new_tourist

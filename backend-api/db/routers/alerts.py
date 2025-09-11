from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import models
from db import get_db

router = APIRouter(prefix="/alerts", tags=["Alerts"])

@router.get("/")
def get_alerts(db: Session = Depends(get_db)):
    return db.query(models.Alert).all()

@router.post("/")
def add_alert(alert: dict, db: Session = Depends(get_db)):
    new_alert = models.Alert(**alert)
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)
    return new_alert

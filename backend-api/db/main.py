from fastapi import FastAPI
from db import Base, engine
import models
from routers import tourists, trips, alerts

app = FastAPI()

# Create tables if not exist
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(tourists.router)
app.include_router(trips.router)
app.include_router(alerts.router)

@app.get("/")
def root():
    return {"message": "Smart Tourist Safety API running 🚀"}

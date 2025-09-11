from fastapi import FastAPI
from pydantic import BaseModel
from anomaly import detect_anomaly
import requests

app = FastAPI(title="AI Service")

# Store tourist location history
tourist_locations = {}

BACKEND_API = "http://127.0.0.1:8000"  # Make sure backend is running at this URL

class LocationPing(BaseModel):
    tourist_id: int
    trip_id: int
    location: str

@app.post("/ping/")
def ping_location(data: LocationPing):
    tid = data.tourist_id
    tourist_locations.setdefault(tid, []).append(data.location)

    # Check for anomalies
    anomaly = detect_anomaly(tourist_locations[tid])
    if anomaly:
        payload = {
            "tourist_id": data.tourist_id,
            "trip_id": data.trip_id,
            "alert_type": "anomaly",
            "description": anomaly,
            "location": data.location
        }

        try:
            # Use a small timeout to prevent hanging if backend is down
            response = requests.post(f"{BACKEND_API}/alerts/", json=payload, timeout=5)
            if response.status_code in [200, 201]:
                print("🚨 Alert sent successfully:", response.json())
            else:
                print("❌ Failed to send alert. Status:", response.status_code, response.text)
        except requests.exceptions.RequestException as e:
            print("❌ Error sending alert:", e)

        return {"status": "anomaly", "message": anomaly}

    return {"status": "ok"}

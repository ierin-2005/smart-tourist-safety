-- 1. Tourists table
CREATE TABLE IF NOT EXISTS tourists (
    id SERIAL PRIMARY KEY,
    digital_id VARCHAR(100) UNIQUE NOT NULL,
    name VARCHAR(100) NOT NULL,
    passport_or_aadhaar VARCHAR(50) NOT NULL,
    phone VARCHAR(20),
    emergency_contact VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Trips table
CREATE TABLE IF NOT EXISTS trips (
    id SERIAL PRIMARY KEY,
    tourist_id INT REFERENCES tourists(id) ON DELETE CASCADE,
    itinerary TEXT,
    start_date DATE,
    end_date DATE,
    safety_score INT DEFAULT 100,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 3. Alerts table
CREATE TABLE IF NOT EXISTS alerts (
    id SERIAL PRIMARY KEY,
    tourist_id INT REFERENCES tourists(id) ON DELETE CASCADE,
    trip_id INT REFERENCES trips(id) ON DELETE CASCADE,
    alert_type VARCHAR(50),   -- panic, anomaly, geofence
    description TEXT,
    location VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Authorities table (if it exists)
CREATE TABLE IF NOT EXISTS authorities (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

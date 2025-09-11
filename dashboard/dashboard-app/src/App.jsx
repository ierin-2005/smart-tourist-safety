import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [alerts, setAlerts] = useState([]);

  const apiUrl = "http://localhost:8000"; // backend FastAPI

  useEffect(() => {
    fetchAlerts();
  }, []);

  const fetchAlerts = async () => {
    try {
      const res = await axios.get(`${apiUrl}/alerts/`);
      setAlerts(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>🚨 Tourist Safety Dashboard</h1>
      <button onClick={fetchAlerts}>Refresh Alerts</button>
      <table border="1" cellPadding="8" style={{ marginTop: "20px" }}>
        <thead>
          <tr>
            <th>ID</th>
            <th>Tourist ID</th>
            <th>Trip ID</th>
            <th>Type</th>
            <th>Description</th>
            <th>Location</th>
            <th>Created</th>
            <th>Resolved?</th>
          </tr>
        </thead>
        <tbody>
          {alerts.map((a) => (
            <tr key={a.id}>
              <td>{a.id}</td>
              <td>{a.tourist_id}</td>
              <td>{a.trip_id}</td>
              <td>{a.alert_type}</td>
              <td>{a.description}</td>
              <td>{a.location}</td>
              <td>{a.created_at}</td>
              <td>{a.resolved ? "✅" : "❌"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default App;

import { useState, useEffect } from 'react'
import './App.css'

interface Machine {
  id: string;
  name: string;
  type: string;
  status: string;
  location: { x: number; y: number };
}

function App() {
  const [machines, setMachines] = useState<Machine[]>([]);
  const [isConnected, setIsConnected] = useState(false);

  useEffect(() => {
    // Fetch machines from backend
    fetch('http://localhost:8000/api/v1/machines')
      .then(res => res.json())
      .then(data => setMachines(data.machines))
      .catch(err => console.error('Error fetching machines:', err));

    // WebSocket connection
    const ws = new WebSocket('ws://localhost:8000/ws/realtime');
    
    ws.onopen = () => {
      setIsConnected(true);
      console.log('WebSocket connected');
    };

    ws.onclose = () => {
      setIsConnected(false);
      console.log('WebSocket disconnected');
    };

    ws.onmessage = (event) => {
      console.log('Received:', event.data);
    };

    return () => ws.close();
  }, []);

  return (
    <div className="App">
      <header>
        <h1>🏭 Intellica</h1>
        <p>AI-Powered Industrial Optimization Platform</p>
        <div className="status">
          <span className={isConnected ? 'connected' : 'disconnected'}>
            {isConnected ? '🟢 Connected' : '🔴 Disconnected'}
          </span>
        </div>
      </header>

      <main>
        <section className="machines">
          <h2>Factory Overview</h2>
          <div className="machine-grid">
            {machines.map((machine) => (
              <div key={machine.id} className="machine-card">
                <h3>{machine.name}</h3>
                <p><strong>Type:</strong> {machine.type}</p>
                <p>
                  <strong>Status:</strong>{' '}
                  <span className={`status-badge ${machine.status}`}>
                    {machine.status}
                  </span>
                </p>
                <p><strong>ID:</strong> {machine.id}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="features">
          <h2>Platform Features</h2>
          <ul>
            <li>✅ Real-time sensor monitoring</li>
            <li>✅ Anomaly detection (96% accuracy)</li>
            <li>✅ Predictive maintenance</li>
            <li>✅ Configuration optimization</li>
            <li>✅ Defect detection with Computer Vision</li>
          </ul>
        </section>
      </main>

      <footer>
        <p>Intellica v1.0.0 | Sənaye 4.0 Hakaton 2025</p>
      </footer>
    </div>
  )
}

export default App
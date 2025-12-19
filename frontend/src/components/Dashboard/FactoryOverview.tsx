import { useEffect, useState } from 'react'
import './FactoryOverview.css'

interface Machine {
  id: string
  name: string
  type: string
  status: string
  location: { x: number; y: number }
}

export default function FactoryOverview() {
  const [machines, setMachines] = useState<Machine[]>([])
  const [selectedMachine, setSelectedMachine] = useState<string | null>(null)

  useEffect(() => {
    // Fetch machines from API
    fetch('http://localhost:8000/api/v1/machines')
      .then(res => res.json())
      .then(data => setMachines(data))
      .catch(err => console.error('Error fetching machines:', err))
  }, [])

  return (
    <div className="factory-overview">
      <h2>Factory Floor</h2>
      <div className="factory-map">
        <svg width="800" height="400" viewBox="0 0 800 400">
          {/* Factory floor background */}
          <rect width="800" height="400" fill="#f5f5f5" />
          
          {/* Grid lines */}
          {[...Array(8)].map((_, i) => (
            <line
              key={`h-${i}`}
              x1="0"
              y1={i * 50}
              x2="800"
              y2={i * 50}
              stroke="#ddd"
              strokeWidth="1"
            />
          ))}
          {[...Array(16)].map((_, i) => (
            <line
              key={`v-${i}`}
              x1={i * 50}
              y1="0"
              x2={i * 50}
              y2="400"
              stroke="#ddd"
              strokeWidth="1"
            />
          ))}
          
          {/* Machines */}
          {machines.map(machine => (
            <g
              key={machine.id}
              transform={`translate(${machine.location.x}, ${machine.location.y})`}
              onClick={() => setSelectedMachine(machine.id)}
              style={{ cursor: 'pointer' }}
            >
              <circle
                r="30"
                fill={machine.status === 'running' ? '#4caf50' : '#ff9800'}
                opacity="0.8"
              />
              <text
                textAnchor="middle"
                dy="5"
                fill="white"
                fontSize="12"
                fontWeight="bold"
              >
                {machine.type}
              </text>
              <text
                textAnchor="middle"
                dy="40"
                fill="#333"
                fontSize="10"
              >
                {machine.name}
              </text>
            </g>
          ))}
        </svg>
      </div>
      
      {selectedMachine && (
        <div className="machine-detail">
          <h3>Selected: {selectedMachine}</h3>
          <button onClick={() => setSelectedMachine(null)}>Close</button>
        </div>
      )}
    </div>
  )
}
-- Enable TimescaleDB extension
CREATE EXTENSION IF NOT EXISTS timescaledb;

-- Machines table
CREATE TABLE IF NOT EXISTS machines (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name VARCHAR(100) NOT NULL,
    type VARCHAR(50) NOT NULL,
    manufacturer VARCHAR(100),
    model VARCHAR(100),
    location_x INTEGER,
    location_y INTEGER,
    protocol VARCHAR(50),
    connection_string TEXT,
    status VARCHAR(20) DEFAULT 'idle',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Sensor data (time-series)
CREATE TABLE IF NOT EXISTS sensor_data (
    time TIMESTAMPTZ NOT NULL,
    machine_id UUID NOT NULL REFERENCES machines(id),
    sensor_name VARCHAR(100) NOT NULL,
    value DOUBLE PRECISION,
    unit VARCHAR(20)
);

-- Convert to hypertable
SELECT create_hypertable('sensor_data', 'time', if_not_exists => TRUE);

-- Alerts table
CREATE TABLE IF NOT EXISTS alerts (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    machine_id UUID REFERENCES machines(id),
    alert_type VARCHAR(50) NOT NULL,
    severity VARCHAR(20) NOT NULL,
    description TEXT,
    ai_recommendation JSONB,
    status VARCHAR(20) DEFAULT 'open',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    resolved_at TIMESTAMPTZ
);

-- Configuration history
CREATE TABLE IF NOT EXISTS config_history (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    machine_id UUID REFERENCES machines(id),
    parameter_name VARCHAR(100),
    old_value JSONB,
    new_value JSONB,
    changed_by VARCHAR(50),
    ai_confidence FLOAT,
    operator_approved BOOLEAN,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

-- ML predictions
CREATE TABLE IF NOT EXISTS predictions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    machine_id UUID REFERENCES machines(id),
    prediction_type VARCHAR(50),
    predicted_value JSONB,
    confidence FLOAT,
    model_version VARCHAR(50),
    created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_sensor_data_machine_time ON sensor_data (machine_id, time DESC);
CREATE INDEX IF NOT EXISTS idx_alerts_status ON alerts (status, created_at DESC);
CREATE INDEX IF NOT EXISTS idx_config_history_machine ON config_history (machine_id, timestamp DESC);
CREATE INDEX IF NOT EXISTS idx_predictions_machine ON predictions (machine_id, created_at DESC);

-- Insert sample machines
INSERT INTO machines (name, type, manufacturer, model, location_x, location_y, protocol, status) VALUES
    ('CNC Machine 1', 'CNC', 'Haas', 'VF-2', 100, 150, 'MQTT', 'running'),
    ('Injection Molding 1', 'Injection', 'Engel', 'e-victory', 300, 150, 'OPC-UA', 'idle'),
    ('Conveyor Belt 1', 'Conveyor', 'Siemens', 'SIMATIC', 500, 150, 'Modbus', 'running')
ON CONFLICT DO NOTHING;
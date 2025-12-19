"""SQLAlchemy Database Models"""
from sqlalchemy import Column, String, Integer, Float, Boolean, DateTime, JSON, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from .database import Base

class Machine(Base):
    __tablename__ = "machines"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(100), nullable=False)
    type = Column(String(50), nullable=False)
    manufacturer = Column(String(100))
    model = Column(String(100))
    location_x = Column(Integer)
    location_y = Column(Integer)
    protocol = Column(String(50))
    connection_string = Column(String)
    status = Column(String(20), default="idle")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    sensor_data = relationship("SensorData", back_populates="machine")
    alerts = relationship("Alert", back_populates="machine")

class SensorData(Base):
    __tablename__ = "sensor_data"
    
    time = Column(DateTime, primary_key=True)
    machine_id = Column(UUID(as_uuid=True), ForeignKey("machines.id"), primary_key=True)
    sensor_name = Column(String(100), primary_key=True)
    value = Column(Float)
    unit = Column(String(20))
    
    # Relationships
    machine = relationship("Machine", back_populates="sensor_data")

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    machine_id = Column(UUID(as_uuid=True), ForeignKey("machines.id"))
    alert_type = Column(String(50), nullable=False)
    severity = Column(String(20), nullable=False)
    description = Column(String)
    ai_recommendation = Column(JSON)
    status = Column(String(20), default="open")
    created_at = Column(DateTime, default=datetime.utcnow)
    resolved_at = Column(DateTime)
    
    # Relationships
    machine = relationship("Machine", back_populates="alerts")

class ConfigHistory(Base):
    __tablename__ = "config_history"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    machine_id = Column(UUID(as_uuid=True), ForeignKey("machines.id"))
    parameter_name = Column(String(100))
    old_value = Column(JSON)
    new_value = Column(JSON)
    changed_by = Column(String(50))
    ai_confidence = Column(Float)
    operator_approved = Column(Boolean)
    timestamp = Column(DateTime, default=datetime.utcnow)

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    machine_id = Column(UUID(as_uuid=True), ForeignKey("machines.id"))
    prediction_type = Column(String(50))
    predicted_value = Column(JSON)
    confidence = Column(Float)
    model_version = Column(String(50))
    created_at = Column(DateTime, default=datetime.utcnow)
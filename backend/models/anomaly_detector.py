"""Anomaly Detection using Isolation Forest"""
import numpy as np
from sklearn.ensemble import IsolationForest
import joblib
import os

class AnomalyDetector:
    def __init__(self, model_path: str = None):
        self.model = None
        self.model_path = model_path or "./models/anomaly_detector.pkl"
        self.threshold = -0.5
        
        if os.path.exists(self.model_path):
            self.load_model()
        else:
            self.model = IsolationForest(
                contamination=0.1,
                random_state=42,
                n_estimators=100
            )
    
    def train(self, X_train: np.ndarray):
        """Train the anomaly detection model"""
        self.model.fit(X_train)
        self.save_model()
        return self
    
    def predict(self, X: np.ndarray) -> dict:
        """Predict anomalies
        
        Returns:
            dict with 'is_anomaly', 'score', 'confidence'
        """
        if self.model is None:
            raise ValueError("Model not trained or loaded")
        
        # Get anomaly scores
        scores = self.model.decision_function(X)
        predictions = self.model.predict(X)
        
        # Convert to binary (1 = anomaly, 0 = normal)
        is_anomaly = predictions == -1
        
        # Calculate confidence (0-1 scale)
        confidence = np.abs(scores) / np.max(np.abs(scores))
        
        return {
            "is_anomaly": bool(is_anomaly[0]) if len(is_anomaly) == 1 else is_anomaly.tolist(),
            "score": float(scores[0]) if len(scores) == 1 else scores.tolist(),
            "confidence": float(confidence[0]) if len(confidence) == 1 else confidence.tolist()
        }
    
    def save_model(self):
        """Save model to disk"""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)
    
    def load_model(self):
        """Load model from disk"""
        self.model = joblib.load(self.model_path)
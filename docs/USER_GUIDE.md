# Intellica User Guide

## Getting Started

### Accessing the Platform

1. Open browser: http://localhost:3000
2. Login with credentials (if auth enabled)
3. View factory dashboard

## Features

### 1. Factory Overview

**What you see:**
- Interactive factory floor map
- Machine status indicators (green=running, orange=idle, red=error)
- Real-time sensor readings

**How to use:**
- Click on any machine to view details
- Hover over sensors for current values
- Watch for alert notifications

### 2. Machine Details

**Information displayed:**
- Current sensor values
- Historical trends (charts)
- Configuration parameters
- Recent alerts

**Actions:**
- View sensor history
- Adjust refresh rate
- Export data

### 3. AI Recommendations

**When you receive a recommendation:**
1. Review the suggestion
2. Check confidence score
3. View expected improvement
4. Approve or reject

**Example:**
```
Title: Reduce Spindle Speed
Confidence: 92%
Expected: 35% vibration reduction

Current: 2500 RPM
Recommended: 2200 RPM

[Approve] [Reject]
```

### 4. Defect Detection

**How to use:**
1. Click "Upload Image"
2. Select product image
3. Wait for analysis (2-3 seconds)
4. View results with bounding boxes

**Interpretation:**
- Normal: No defects found
- Crack/Scratch/Deformation: Defect type and location
- Confidence score: Model certainty

### 5. Analytics Dashboard

**Metrics explained:**
- **OEE**: Overall Equipment Effectiveness (target: >85%)
- **Availability**: Machine uptime percentage
- **Performance**: Speed vs. design speed
- **Quality**: Good products / total products
- **Downtime**: Hours of non-operation
- **Defect Rate**: Percentage of defective products

## Alerts

### Alert Types
- 🟢 Info: General notifications
- 🟡 Warning: Attention needed
- 🔴 Critical: Immediate action required

### Alert Actions
1. Click notification to view details
2. Acknowledge alert
3. Take corrective action
4. Mark as resolved

## Best Practices

1. **Monitor regularly**: Check dashboard every 15 minutes
2. **Act on alerts**: Don't ignore critical alerts
3. **Review AI recommendations**: Evaluate before approving
4. **Analyze trends**: Use analytics to identify patterns
5. **Document changes**: Add notes when applying configs

## Troubleshooting

### No data showing
- Check network connection
- Verify backend is running
- Refresh page (F5)

### Sensor data delayed
- Check MQTT connection
- Verify simulator is running
- Check backend logs

### Can't approve recommendation
- Check user permissions
- Verify recommendation is still valid
- Contact administrator
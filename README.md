

## Overview

This repository contains the code and dataset for predicting Air Quality Index (AQI) using a Long Short-Term Memory (LSTM) model. The dataset includes three files: `city_data.csv`, `city_hour.csv`, and `station_day.csv`. Additionally, the repository includes a Jupyter Notebook (`PCB-PM.ipynb`) for the solution implementation and an IoT Python script (`iot.py`) for real-time AQI monitoring.

## Dataset

- `city_data.csv`
- `city_hour.csv`
- `station_day.csv`

## Solution Implementation

### Jupyter Notebook

- File: `PCB-PM.ipynb`
- This Jupyter Notebook implements the LSTM model for predicting AQI.
- The notebook includes detailed explanations, visualizations, and evaluations of the model.
- **Usage:**
  - Ensure that you have the necessary dependencies installed (listed in the notebook).
  - Open and run the notebook in a Jupyter environment.

## Real-Time AQI Monitoring

### IoT Script

- File: `iot.py`
- This Python script monitors real-time air quality using a DHT11 sensor and an analog sensor.
- The script categorizes PM concentration levels and sends the data to a specified server endpoint.
- **Requirements:**
  - Python
  - Micropython
  - DHT Library
- **Usage:**
  - Connect the DHT11 sensor and analog sensor to your IoT device.
  - Update the `YOUR_SERVER_ENDPOINT` variable with the appropriate server endpoint.
  - Run the script on your IoT device.

### Script Overview

The `iot.py` script reads data from a DHT11 sensor and an analog sensor to monitor air quality. It categorizes PM concentration levels and sends the data to a server endpoint.

#### ***PM Level Categorization***

The PM concentration is categorized as follows:

Good: Concentration < 50
Moderate: 50 <= Concentration < 100
Unhealthy for Sensitive Groups: 100 <= Concentration < 150
Unhealthy: 150 <= Concentration < 200
Very Unhealthy: 200 <= Concentration < 300
Hazardous: Concentration >= 300

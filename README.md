# Real-Time Market Signals & Alerts Platform

## Overview
A real-time, end-to-end market signal system that ingests live stock data, 
computes short-term indicators, ranks opportunities, and generates confidence-based alerts.

This project is designed as a portfolio example demonstrating production-style
data ingestion, signal generation, alerting logic, and API design for real-time systems.


## Architecture
Yahoo Finance → Feature Extraction → Opportunity & Confidence Scoring  
→ Alert Logic → FastAPI (JSON APIs) → Streamlit UI

## Features
- Real-time ingestion (Yahoo Finance)
- Feature extraction: momentum, volatility, volume spike
- Opportunity + confidence scoring
- Alerts (LOW/MEDIUM/HIGH) with reasons
- FastAPI endpoints with Swagger UI
- Streamlit UI to visualize alerts

## Screenshots
(Swagger)
docs/images/01_Swagger_UI_home
docs/images/02_Swagger_UI_Get
docs/images/03_Swagger_UI_Response
docs/images/04_Swagger_UI_Get_alerts
docs/images/05_Swagger_UI_Get_alerts_response
(Streamlit)
06_Streamlit_alerts_indicator

## How to Run Locally
1. Clone the repo
2. pip install -r requirements.txt
3. uvicorn api:app --reload
   Swagger API Docs: http://localhost:8000/docs
4. streamlit run ui/alerts_app.py


## Future Improvements
- Alert cooldown and deduplication
- Backtesting and performance metrics
- Short-horizon forecasting models
- Persistent storage for alerts
   
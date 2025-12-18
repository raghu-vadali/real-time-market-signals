# Real-Time Market Signals & Alerts Platform

## Overview
End-to-end system that ingests live stock data, computes short-term signals,
ranks opportunities, and generates confidence-based alerts.

## Architecture
(FastAPI → Services → Alerts → Streamlit UI)

## Features
- Real-time ingestion (Yahoo Finance)
- Momentum & volatility signals
- Opportunity & confidence scoring
- Alert generation with severity
- REST API with Swagger
- Streamlit Alerts UI

## Screenshots
(Swagger)
(Streamlit)

## How to Run Locally
1. Clone the repo
2. pip install -r requirements.txt
3. uvicorn api:app --reload
4. streamlit run ui/alerts_app.py
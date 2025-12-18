# api.py
from fastapi import FastAPI, Query
from datetime import datetime
from dataclasses import asdict, is_dataclass

from ingestion.market_data_provider import YahooMarketDataProvider
from features.realtime_features import RealtimeFeatureExtractor
from scoring.opportunity_scorer import OpportunityScorer
from services.overview_service import OverviewService
from services.alert_service import AlertService

app = FastAPI(title="Real-Time Stock Forecasting (Overview API)")

service = OverviewService(
    provider=YahooMarketDataProvider(),
    extractor=RealtimeFeatureExtractor(),
    scorer=OpportunityScorer()
)

def to_json(obj):
    # SymbolSnapshot is a dataclass; convert safely to JSON-friendly dict
    if is_dataclass(obj):
        d = asdict(obj)
        # datetime -> ISO string
        if isinstance(d.get("timestamp"), datetime):
            d["timestamp"] = d["timestamp"].isoformat()
        return d
    return obj

@app.get("/overview")
def overview(symbols: str = Query(..., description="Comma-separated symbols e.g. AAPL,MSFT,TSLA")):
    symbol_list = [s.strip().upper() for s in symbols.split(",") if s.strip()]
    snapshots = service.overview(symbol_list)
    return [to_json(s) for s in snapshots]

@app.get("/alerts")
def get_alerts(symbols: str = Query(..., description="Comma-separated symbols e.g. AAPL,MSFT,TSLA")):
    symbol_list = [s.strip().upper() for s in symbols.split(",") if s.strip()]
    snapshots = service.overview(symbol_list)
    alert_service = AlertService()
    alerts = alert_service.generate_alerts(snapshots)
    return alerts
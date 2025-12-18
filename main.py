import numpy as np
import pandas as pd
from ingestion.market_data_provider import YahooMarketDataProvider
from features.realtime_features import RealtimeFeatureExtractor
from scoring.opportunity_scorer import OpportunityScorer
from services.overview_service import OverviewService
from models.symbol_snapshot import SymbolSnapshot
from services.alert_service import AlertService
 
symbols = ["AAPL", "MSFT", "TSLA"]
provider = YahooMarketDataProvider()
extractor = RealtimeFeatureExtractor()
scorer = OpportunityScorer()
service = OverviewService(provider, extractor, scorer)

snapshots = service.overview(symbols)  

for i, s in enumerate(snapshots, start=1):
    print(f"{i}. {s.symbol} → score={s.opportunity_score}, confidence={s.confidence}, price={s.price}, trend={s.trend}")
    
alert_service = AlertService()
alerts = alert_service.generate_alerts(snapshots)

print("\n=== ALERTS ===")
for a in alerts:
    print(
        f"{a.severity} | {a.symbol} | {a.alert_type} | "
        f"score={a.opportunity_score} | conf={a.confidence} | {a.reason}"
    )
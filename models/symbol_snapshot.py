# src/models/symbol_snapshot.py
from dataclasses import dataclass
from datetime import datetime

@dataclass
class SymbolSnapshot:
    symbol: str
    price: float
    pct_change: float
    momentum: float
    volatility: float
    volume: int
    volume_spike: float
    trend: str
    opportunity_score: float
    confidence: float
    sparkline_prices: list[float]
    sparkline_times: list[str]
    timestamp: datetime

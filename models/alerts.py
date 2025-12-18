from dataclasses import dataclass
from datetime import datetime

@dataclass
class Alert:
    symbol: str
    alert_type: str        # e.g. BREAKOUT, MOMENTUM, VOLUME
    severity: str          # LOW / MEDIUM / HIGH
    opportunity_score: float
    confidence: float
    reason: str
    timestamp: datetime
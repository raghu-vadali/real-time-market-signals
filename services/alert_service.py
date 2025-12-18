from datetime import datetime, timezone
from models.alerts import Alert
from models.symbol_snapshot import SymbolSnapshot


class AlertService:
    def generate_alerts(self, snapshots: list[SymbolSnapshot]) -> list[Alert]:
        alerts: list[Alert] = []

        for s in snapshots:
            # HIGH severity alert
            if (
                s.opportunity_score >= 0.6
                and s.confidence >= 0.7
                and s.trend != "FLAT"
            ):
                alerts.append(
                    Alert(
                        symbol=s.symbol,
                        alert_type="BREAKOUT",
                        severity="HIGH",
                        opportunity_score=s.opportunity_score,
                        confidence=s.confidence,
                        reason="Strong opportunity with high confidence and clear trend",
                        timestamp=datetime.now(timezone.utc),
                    )
                )
                continue  # avoid duplicate alerts for same symbol

            # MEDIUM severity alert
            if s.opportunity_score >= 0.4 and s.confidence >= 0.6:
                alerts.append(
                    Alert(
                        symbol=s.symbol,
                        alert_type="MOMENTUM",
                        severity="MEDIUM",
                        opportunity_score=s.opportunity_score,
                        confidence=s.confidence,
                        reason="Moderate opportunity with good confidence",
                        timestamp=datetime.now(timezone.utc),
                    )
                )
                continue

            # LOW severity alert (volume anomaly only)
            if s.volume_spike >= 3:
                alerts.append(
                    Alert(
                        symbol=s.symbol,
                        alert_type="VOLUME",
                        severity="LOW",
                        opportunity_score=s.opportunity_score,
                        confidence=s.confidence,
                        reason="Unusual volume detected",
                        timestamp=datetime.now(timezone.utc),
                    )
                )

        return alerts

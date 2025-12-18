# src/services/overview_service.py

from models.symbol_snapshot import SymbolSnapshot
from features.sparkline import build_sparkline
from datetime import datetime, timezone

class OverviewService:
    def __init__(self, provider, extractor, scorer):
        self.provider = provider
        self.extractor = extractor
        self.scorer = scorer
        self._cache: dict[tuple[str, str], SymbolSnapshot] = {}

    def snapshot(self, symbol: str):
        now_minute = datetime.now(timezone.utc).replace(second=0, microsecond=0)
        cache_key = (symbol, now_minute.isoformat())
        
        cached = self._cache.get(cache_key)
        if cached is not None:
            return cached
        
        df = self.provider.get_latest(symbol)
        spark_prices, spark_times = build_sparkline(df, points=30)
        features = self.extractor.compute(df)
        trend = self.extractor.classify_trend(
                features["momentum"], features["volatility"]
                )
        confidence = (
                0.5 * (1 - min(features["volatility"] / 0.01, 1.0)) +
                0.3 * min(features["volume_spike"] / 3.0, 1.0) +
                0.2 * (1 if trend != "FLAT" else 0)
                )
        confidence = round(max(0.0, min(confidence, 1.0)), 3)
        
        snap = SymbolSnapshot(            
                symbol=symbol,
                price=round(features["price"], 2),
                pct_change=features["pct_change"],
                momentum=features["momentum"],
                volatility=features["volatility"],
                volume=features["volume"],
                volume_spike=features["volume_spike"],
                trend=trend,
                opportunity_score=self.scorer.score(features),
                confidence=confidence,                
                sparkline_prices=spark_prices,
                sparkline_times=spark_times,
                timestamp=datetime.now(timezone.utc)
            )
        self._cache[cache_key] = snap   # ⬅️ STORE
        return snap                     # ⬅️ RETURN
        
    def overview(self, symbols: list[str]) -> list[SymbolSnapshot]:
        snapshots: list[SymbolSnapshot] = []

        for symbol in symbols:
            try:
                snapshot = self.snapshot(symbol)
                snapshots.append(snapshot)
            except Exception as e:
                # Fail-safe: one symbol should not break the page
                print(f"[WARN] Failed to process {symbol}: {e}")

        # Rank by opportunity_score (highest first)
        snapshots.sort(
            key=lambda s: s.opportunity_score,
            reverse=True
        )

        return snapshots 
# src/features/realtime_features.py

import numpy as np

class RealtimeFeatureExtractor:

    def compute(self, df):
        df = df.copy()
        
        # financial metrics/features calculation
        df["return_1m"] = df["Close"].pct_change()
        df["momentum"] = df["Close"].pct_change(5)
        df["volatility"] = df["return_1m"].rolling(20).std()
        df["volume_z"] = ((df["Volume"] - df["Volume"].rolling(20).mean())
                           / df["Volume"].rolling(20).std()
                         )

        latest = df.iloc[-1]

        return {
            "price": float(latest["Close"].iloc[0]),
            "pct_change": float(latest["return_1m"].iloc[0]),
            "momentum": float(latest["momentum"].iloc[0]),
            "volatility": float(latest["volatility"].iloc[0]),
            "volume": int(latest["Volume"].iloc[0]),
            "volume_spike": float(latest["volume_z"].iloc[0]),
        }
        
    # Add Trend Classification momentum and volatility
    def classify_trend(self, momentum, volatility):
        if abs(momentum) < volatility * 0.5:
            return "FLAT"
        return "UP" if momentum > 0 else "DOWN"   




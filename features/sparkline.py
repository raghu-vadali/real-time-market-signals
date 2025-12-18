# Graphs (Overview sparklines
import pandas as pd

def build_sparkline(df, points: int = 30):
    tail = df.tail(points)
    
     # Prices (always safe)
    prices = [round(float(x), 2) for x in tail["Close"].values]
    
    # Timestamps (handle both cases)
    if hasattr(tail.index, "to_pydatetime"):
        times = [t.isoformat() for t in tail.index.to_pydatetime()]
    else:
        # Fallback: use row numbers as pseudo-time
        times = [str(i) for i in range(len(prices))]

    return prices, times

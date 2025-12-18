# src/ingestion/market_data_provider.py
import yfinance as yf

class YahooMarketDataProvider:
    def get_latest(self, symbol: str, period: str = "1d", interval: str = "1m"):
        df = yf.download(symbol, period=period, interval=interval, auto_adjust=False)
        return df   






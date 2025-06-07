import yfinance as yf

def load_stock_data(ticker="AAPL", start="2022-01-01", end="2024-01-01"):
    data = yf.download(ticker, start=start, end=end)
    # flatten MultiIndex columns
    data.columns = [col[0] if isinstance(col, tuple) else col for col in data.columns]
    data.dropna(inplace=True)
    return data

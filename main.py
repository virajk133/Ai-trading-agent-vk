from data_loader import load_stock_data
from strategy import add_indicators
from model import train_model
from utils import backtest
import matplotlib.pyplot as plt

df = load_stock_data("AAPL")
df = add_indicators(df)
model = train_model(df)
results = backtest(df, model)

results[['Daily_Return', 'Strategy_Return']].cumsum().plot(figsize=(10,6))
plt.title("Cumulative Returns: Strategy vs Market")
plt.grid()
plt.show()

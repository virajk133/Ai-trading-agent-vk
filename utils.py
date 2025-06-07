def backtest(df, model):
    df['Predicted'] = model.predict(df[['SMA_10', 'SMA_50']])
    df['Daily_Return'] = df['Close'].pct_change()
    df['Strategy_Return'] = df['Daily_Return'] * df['Predicted'].shift(1)
    print(df.columns)
    return df[['Close', 'Daily_Return', 'Strategy_Return']].dropna()
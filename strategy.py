def add_indicators(df) :
    df['SMA_10'] = df['Close'].rolling(window=10).mean()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['signal'] = 0
    df.loc[df['SMA_10'] > df['SMA_50'], 'signal'] = 1
    df.loc[df['SMA_10'] < df['SMA_50'], 'signal'] = -1
    return df.dropna()
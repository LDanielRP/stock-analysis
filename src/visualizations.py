import matplotlib.pyplot as plt


def plot_price_with_indicators(df, ticker):
    plt.figure(figsize=(14, 7))
    plt.plot(df['Close'], label='Close Price', linewidth=1.5)

    if 'SMA_20' in df.columns:
        plt.plot(df['SMA_20'], label='SMA 20', linestyle='--')

    if 'EMA_20' in df.columns:
        plt.plot(df['EMA_20'], label='EMA_20', linestyle='--')

    plt.title(f'{ticker} - Price with SMA & EMA')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_rsi(df, ticker):
    plt.figure(figsize=(14, 4))
    plt.plot(df['RSI_14'], label='RSI 14', color='purple')

    plt.axhline(70, linestyle='--', color='red', label='Overbought (70)')
    plt.axhline(30, linestyle='--', color='green', label='Oversold (30)')

    plt.title(f'{ticker} - RSI Indicator')
    plt.xlabel('Date')
    plt.ylabel('RSI')

    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

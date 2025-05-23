from fetch_data import download_stock_data
from indicators import calculate_sma, calculate_ema, calculate_rsi
from visualizations import plot_price_with_indicators, plot_rsi
import yfinance as fg


def main():
    ticker = 'AAPL'
    df = download_stock_data(ticker)

    df = calculate_sma(df, period=20)
    df = calculate_ema(df, period=20)
    df = calculate_rsi(df, period=14)

    plot_price_with_indicators(df, ticker)
    plot_rsi(df, ticker)


if __name__ == '__main__':
    main()

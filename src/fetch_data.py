import yfinance as yf
import pandas as pd


def download_stock_data(ticker="AAPL", start_date="2020-01-01", end_date="2024-12-31"):
    df = yf.download(ticker, start=start_date, end=end_date)
    df.reset_index(inplace=True)
    return df


if __name__ == "__main__":
    data = download_stock_data("AAPL")
    print(data.head())

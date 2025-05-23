import pandas as pd


def calculate_sma(df, period=20, column='Close'):
    """
    Calculates the Simple Moving Average (SMA).
    :param df: DataFrame with stock data
    :param period: number of days for moving average
    :param column: which colum to calculate SMA on
    :return: DataFrame with new 'SMA_{period}' column
    """
    df[f'SMA_{period}'] = df[column].rolling(window=period).mean()
    return df


def calculate_ema(df, period=20, column='Close'):
    """
    Calculate the Exponential Moving Average (EMA).
    :param df: DataFrame with stock data
    :param period: number of days
    :param column: price column (usually 'Close')
    :return: DataFrame with new 'EMA_{period}' column
    """
    df[f'EMA_{period}'] = df[column].ewm(span=period, adjust=False).mean()
    return df


def calculate_rsi(df, period=14, column='Close'):
    """
    Calculates the Relative Strength Index (RSI).
    RSI is a momentum indicator used to identify overbought or oversold conditions.
    :param df: DataFrame with stock data
    :param period: Number of periods to use for RSI
    :param column: Price column
    :return: DataFrame with new 'RSI_{period}' column
    """
    delta = df[column].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    df[f'RSI_{period}'] = rsi
    return df

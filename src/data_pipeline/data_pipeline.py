import pandas as pd
import yfinance as yf

def fetch_stock_data(stock, period = '5y'):
    ticker_name = yf.Ticker(stock)
    data = ticker_name.history(period = period)

    dtf = data[['Open', 'High', 'Low', 'Close', 'Volume']].copy()
    dtf.index = dtf.index.date
    dtf.index.name = 'Date'

    return dtf

def engineer_features(df):
    df['Return_5Day'] = df['Close'].pct_change(5)
    df['SMA200'] = df['Close'].rolling(200).mean()
    df['Distance_SMA200'] = (df['Close'] - df['SMA200']) / df['SMA200']
    df['Actual_Future_Return'] = df['Return_5Day'].shift(-5)
    df.drop(columns = ['SMA200'], inplace = True)

    return df

tickers = ['POWERGRID.NS', 'ADANIPOWER.NS', 'HINDCOPPER.NS', 'NTPC.NS', 'TATAPOWER.NS']

all_dfs = []
for ticker in tickers:
    df = fetch_stock_data(ticker)
    df = engineer_features(df)
    df = df.reset_index()
    df['Ticker'] = ticker
    all_dfs.append(df)

final_df = pd.concat(all_dfs, ignore_index=True)
final_df.to_csv('./data_pipeline.csv', index = False)
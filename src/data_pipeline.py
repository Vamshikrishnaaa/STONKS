import pandas as pd
import yfinance as yf

# ATHER ENERGY

def cleaned_stock1():
    ticker1 = yf.Ticker('ATHERENERG.NS')
    info1 = ticker1.history(period='1y')

    ohlcv_df = info1[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

    ohlcv_df.index = ohlcv_df.index.date
    ohlcv_df.index.name = 'Date'

    ohlcv_df.columns = [f"{col}" for col in ohlcv_df.columns]

    print(ohlcv_df)

    return ohlcv_df


# ADANI POWER

def cleaned_stock2():
    ticker2 = yf.Ticker('ADANIPOWER.NS')
    info2 = ticker2.history(period='1y')

    ohlcv_df = info2[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

    ohlcv_df.index = ohlcv_df.index.date
    ohlcv_df.index.name = 'Date'

    ohlcv_df.columns = [f"{col}" for col in ohlcv_df.columns]

    print("\n--- ADANIPOWER.NS Full Data ---")
    print(ohlcv_df)
    return ohlcv_df

# HINDUSTAN COPPER

def cleaned_stock3():
    ticker3 = yf.Ticker('HINDCOPPER.NS')
    info3 = ticker3.history(period='1y')

    ohlcv_df = info3[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

    ohlcv_df.index = ohlcv_df.index.date
    ohlcv_df.index.name = 'Date'

    ohlcv_df.columns = [f"{col}" for col in ohlcv_df.columns]

    print("\n--- HINDCOPPER.NS Full Data ---")
    print(ohlcv_df)
    return ohlcv_df


# NTPC

def cleaned_stock4():
    ticker4 = yf.Ticker('NTPC.NS')
    info4 = ticker4.history(period='1y')

    ohlcv_df = info4[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

    ohlcv_df.index = ohlcv_df.index.date
    ohlcv_df.index.name = 'Date'

    ohlcv_df.columns = [f"{col}" for col in ohlcv_df.columns]

    print("\n--- NTPC.NS Full Data ---")
    print(ohlcv_df)
    return ohlcv_df

# TATA POWER

def cleaned_stock5():
    ticker5 = yf.Ticker('TATAPOWER.NS')
    info5 = ticker5.history(period='1y')

    ohlcv_df = info5[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

    ohlcv_df.index = ohlcv_df.index.date
    ohlcv_df.index.name = 'Date'

    ohlcv_df.columns = [f"{col}" for col in ohlcv_df.columns]

    print("\n--- TATAPOWER.NS Full Data ---")
    print(ohlcv_df)
    return ohlcv_df



# Function calls

cleaned_stock1()
#cleaned_stock2()
#cleaned_stock3()
#cleaned_stock4()
#cleaned_stock5()
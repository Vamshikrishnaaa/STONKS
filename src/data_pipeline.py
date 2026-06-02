import pandas as pd
import yfinance as yf

# ATHER ENERGY

def ATHERENERG():
    ticker1 = yf.Ticker('ATHERENERG.NS')
    info1 = ticker1.history(period='1y')

    ohlcv_df = info1[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

    ohlcv_df.index = ohlcv_df.index.date
    ohlcv_df.index.name = 'Date'

    ohlcv_df.columns = [f"{col}" for col in ohlcv_df.columns]

    print(ohlcv_df)

    return ohlcv_df


# ADANI POWER

def ADANIPOWER():
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

def HINDCOPPER():
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

def NTPC():
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

def TATAPOWER():
    ticker5 = yf.Ticker('TATAPOWER.NS')
    info5 = ticker5.history(period='1y')

    ohlcv_df = info5[['Open', 'High', 'Low', 'Close', 'Volume']].copy()

    ohlcv_df.index = ohlcv_df.index.date
    ohlcv_df.index.name = 'Date'

    ohlcv_df.columns = [f"{col}" for col in ohlcv_df.columns]

    print("\n--- TATAPOWER.NS Full Data ---")
    print(ohlcv_df)
    return ohlcv_df





# 1. Capture the dataframes returned by your functions
df1 = ATHERENERG()
df2 = ADANIPOWER()
df3 = HINDCOPPER()
df4 = NTPC()
df5 = TATAPOWER()


df1 = df1.reset_index()
df1['Ticker'] = 'ATHERENERG.NS'

df2 = df2.reset_index()
df2['Ticker'] = 'ADANIPOWER.NS'

df3 = df3.reset_index()
df3['Ticker'] = 'HINDCOPPER.NS'

df4 = df4.reset_index()
df4['Ticker'] = 'NTPC.NS'

df5 = df5.reset_index()
df5['Ticker'] = 'TATAPOWER.NS'


final_df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)


final_df.to_csv('final_data.csv', index=False, sep=',')

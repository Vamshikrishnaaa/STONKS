import pandas as pd # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore

data = pd.read_csv('../data/processed/market_data.csv')
tickers = ['POWERGRID.NS', 'ADANIPOWER.NS', 'HINDCOPPER.NS', 'NTPC.NS', 'TATAPOWER.NS']

data = data.dropna()

train_df = []
test_df = []

rows_per_stock = data.shape[0]//5
train_rows_per_stock = round(0.8 * rows_per_stock)
test_rows_per_stock = rows_per_stock - train_rows_per_stock

def split_tickers(ticker_name):
    train = data.loc[data['Ticker'] == ticker_name].head(train_rows_per_stock)
    test = data.loc[data['Ticker'] == ticker_name].iloc[train_rows_per_stock : train_rows_per_stock+test_rows_per_stock]
    train_df.append(train)
    test_df.append(test)

for ticker in tickers:
    split_tickers(ticker)

final_train_df = pd.concat(train_df, ignore_index=True)
final_test_df = pd.concat(test_df, ignore_index=True)

X_train = final_train_df[['Return_5Day', 'Distance_SMA200']]
y_train = final_train_df['Actual_Future_Return']

X_test = final_test_df[['Return_5Day', 'Distance_SMA200']]
y_test = final_test_df['Actual_Future_Return']

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)

y_pred = lin_reg.predict(X_test)

final_test_df['Predicted_Return'] = y_pred

mean_final_test = final_test_df.groupby('Ticker').Predicted_Return.mean()
mean_actual = final_test_df.groupby('Ticker').Actual_Future_Return.mean()

df = pd.DataFrame(mean_final_test).reset_index()
df2 = pd.DataFrame(mean_actual).reset_index()

result = pd.merge(df, df2)

final_rankings = result.sort_values(by='Predicted_Return', ascending = False)

final_rankings.to_csv('../data/processed/final_rankings.csv', index = False)
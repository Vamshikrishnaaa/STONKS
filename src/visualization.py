import matplotlib.pyplot as plt # type: ignore
import pandas as pd  # type: ignore

df=pd.read_csv('../data/processed/final_rankings.csv')

x=list(df['Predicted_Return'])
y=list(df['Actual_Future_Return'])

plt.plot(x,y,marker='o',markersize='4')
plt.show()

tickers=list(df['Ticker'])
plt.bar(tickers,x,width=0.6,color='blue')
plt.show()
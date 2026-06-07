import matplotlib.pyplot as plt 
import pandas as pd  

df=pd.read_csv('../data/processed/final_rankings.csv')

plt.barh(df['Ticker'], df['Predicted_Return'])
plt.xlabel('Predicted Return')
plt.title('Predicted Stock Rankings')
plt.tight_layout()
plt.savefig('../graphs/pred_graph.png')
plt.show()

plt.barh(df['Ticker'], df['Actual_Future_Return'])
plt.xlabel('Actual Return')
plt.title('Actual Stock Rankings')
plt.tight_layout()
plt.savefig('../graphs/actual_graph.png')
plt.show()
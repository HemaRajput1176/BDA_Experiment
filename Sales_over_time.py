import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dates = pd.date_range(start='2024-01-01', periods=10)
sales = [1200,1500,1700,1600,1800,2000,2100,2200,2500,2400]

df = pd.DataFrame({'Date': dates, 'Sales': sales})
df['t'] = np.arange(len(df))

coef = np.polyfit(df['t'], df['Sales'], 1)
df['Trend'] = np.poly1d(coef)(df['t'])

plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Sales'], label='Actual Sales')
plt.plot(df['Date'], df['Trend'], label='Trend Line')

plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trend Over Time')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
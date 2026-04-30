import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Date': pd.date_range(start='2024-01-01', periods=10),
    'Close': [150,152,148,155,160,158,162,165,170,168]
}

df = pd.DataFrame(data)

df['MA_3'] = df['Close'].rolling(3).mean()
df['MA_5'] = df['Close'].rolling(5).mean()

plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Close'], label='Original Price')
plt.plot(df['Date'], df['MA_3'], label='3-Day MA')
plt.plot(df['Date'], df['MA_5'], label='5-Day MA')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Moving Average Smoothing')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
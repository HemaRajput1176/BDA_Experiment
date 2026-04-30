import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load data from CSV
data = pd.read_csv('stock_prices.csv')

# Step 2: Convert Date column into datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Step 3: Sort data by Date (important for time series)
data = data.sort_values(by='Date')

# Step 4: Plot line chart
plt.figure(figsize=(10, 5))
plt.plot(data['Date'], data['Close'])

# Step 5: Add labels and title
plt.xlabel('Date')
plt.ylabel('Closing Price')
plt.title('Stock Price Trend Over Time')

# Step 6: Rotate dates for better visibility
plt.xticks(rotation=45)

# Step 7: Show grid (helps in reading values)
plt.grid(True)

# Step 8: Display the chart
plt.tight_layout()
plt.show()
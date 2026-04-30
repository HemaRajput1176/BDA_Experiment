import pandas as pd
import matplotlib.pyplot as plt

# Show all rows/columns clearly (optional)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Load dataset
df = pd.read_csv("sales.csv")

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Create Revenue column
df['Revenue'] = df['Price'] * df['Quantity']

# Verify data
print(df)
print("\nShape of dataset:", df.shape)
# Sales by Category (Bar Chart)

category_sales = df.groupby('Category')['Revenue'].sum()

plt.figure()
category_sales.plot(kind='bar')
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.title("Sales by Category")
plt.show()

print(category_sales)
# Monthly Sales Trend (Time-Series)

monthly_sales = df.resample('ME', on='Date')['Revenue'].sum()

plt.figure()
monthly_sales.plot(marker='o')
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.title("Monthly Sales Trend")
plt.show()

print(monthly_sales)
# Top Selling Products

product_sales = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False)

plt.figure()
product_sales.plot(kind='bar')
plt.xlabel("Product")
plt.ylabel("Total Revenue")
plt.title("Top Selling Products")
plt.show()

print(product_sales)
# Sales by City

city_sales = df.groupby('City')['Revenue'].sum().sort_values(ascending=False)

plt.figure()
city_sales.plot(kind='bar')
plt.xlabel("City")
plt.ylabel("Total Revenue")
plt.title("Sales by City")
plt.show()

print(city_sales)
# Quantity Sold per Category

qty_per_category = df.groupby('Category')['Quantity'].sum()

plt.figure()
qty_per_category.plot(kind='bar')
plt.xlabel("Category")
plt.ylabel("Total Quantity Sold")
plt.title("Quantity Sold per Category")
plt.show()

print(qty_per_category)
# Moving Average (Advanced Temporal)

monthly_sales = df.resample('M', on='Date')['Revenue'].sum().sort_values(ascending=False)

moving_avg = monthly_sales.rolling(window=2).mean()

plt.figure()
monthly_sales.plot(marker='o', label='Monthly Sales')
moving_avg.plot(marker='o', label='Moving Average (2 months)')
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Monthly Sales with Moving Average")
plt.legend()
plt.show()

print(moving_avg)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales_data = pd.read_csv("sales_data.csv")

sales_data.dropna(subset=['Order Date', 'Sales', 'Product', 'Region'], inplace=True)
sales_data['Order Date'] = pd.to_datetime(sales_data['Order Date'])
sales_data['Month'] = sales_data['Order Date'].dt.month

monthly_sales = sales_data.groupby('Month')['Sales'].sum()

plt.figure(figsize=(10, 6))
plt.plot(monthly_sales, marker='o', color='b')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.show()

product_sales = sales_data.groupby('Product')['Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))
product_sales[:10].plot(kind='bar', color='skyblue')
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

region_sales = sales_data.groupby('Region')['Sales'].sum()

plt.figure(figsize=(8, 6))
region_sales.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title("Sales by Region")
plt.ylabel("")
plt.show()

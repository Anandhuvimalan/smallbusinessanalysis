import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory for plots if it doesn't exist
output_dir = 'analysis'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Load Data
print("Loading data...")
try:
    df = pd.read_csv('data/coffee_shop_sales.csv')
except FileNotFoundError:
    print("Error: data/coffee_shop_sales.csv not found. Please run generate_data.py first.")
    exit()

# Preprocessing
print("Preprocessing data...")
df['date'] = pd.to_datetime(df['date'])
df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
df['month'] = df['date'].dt.to_period('M')
df['hour'] = df['datetime'].dt.hour
df['day_of_week'] = df['date'].dt.day_name()

# --- Analysis & Visualizations ---

# Set style
sns.set_theme(style="whitegrid")

# 1. Sales Trend over Time (Monthly)
print("Generating Sales Trend Analysis...")
monthly_sales = df.groupby('month')['total_price'].sum()
plt.figure(figsize=(12, 6))
monthly_sales.plot(kind='line', marker='o', color='b')
plt.title('Total Revenue by Month')
plt.ylabel('Revenue ($)')
plt.xlabel('Month')
plt.grid(True)
plt.savefig(f'{output_dir}/monthly_sales_trend.png')
plt.close()

# 2. Peak Hours Analysis
print("Generating Peak Hours Analysis...")
hourly_sales = df.groupby('hour')['total_price'].sum()
plt.figure(figsize=(10, 6))
sns.barplot(x=hourly_sales.index, y=hourly_sales.values, palette="viridis")
plt.title('Total Sales by Hour of Day')
plt.ylabel('Total Sales ($)')
plt.xlabel('Hour (24h)')
plt.savefig(f'{output_dir}/hourly_sales.png')
plt.close()

# 3. Sales by Category
print("Generating Category Analysis...")
category_sales = df.groupby('category')['total_price'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 8))
plt.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Revenue Distribution by Category')
plt.savefig(f'{output_dir}/category_distribution.png')
plt.close()

# 4. Top 5 Best Selling Products
print("Generating Top Products Analysis...")
top_products = df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(5)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette="magma")
plt.title('Top 5 Best Selling Products (Quantity)')
plt.xlabel('Quantity Sold')
plt.savefig(f'{output_dir}/top_5_products.png')
plt.close()

# 5. Sales by Store Location
print("Generating Store Analysis...")
store_sales = df.groupby('store_location')['total_price'].sum()
plt.figure(figsize=(8, 6))
sns.barplot(x=store_sales.index, y=store_sales.values, palette="coolwarm")
plt.title('Total Revenue by Store Location')
plt.ylabel('Revenue ($)')
plt.savefig(f'{output_dir}/store_performance.png')
plt.close()


# --- Summary Report ---
print("\n" + "="*30)
print("     EXECUTIVE SUMMARY     ")
print("="*30)
print(f"Total Transactions: {len(df)}")
print(f"Total Revenue: ${df['total_price'].sum():,.2f}")
print(f"Average Transaction Value: ${df['total_price'].mean():.2f}")
print(f"Best Selling Category: {category_sales.idxmax()} (${category_sales.max():,.2f})")
print(f"Most Popular Product: {top_products.idxmax()} ({top_products.max()} units)")
print(f"Top Performing Store: {store_sales.idxmax()} (${store_sales.max():,.2f})")
print("="*30)
print(f"Analysis complete. Visualizations saved to '{output_dir}/' directory.")

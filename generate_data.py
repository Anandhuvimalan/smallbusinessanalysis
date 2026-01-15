import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Configuration
NUM_TRANSACTIONS = 10000
START_DATE = datetime(2025, 1, 1)
END_DATE = datetime(2025, 12, 31)

# Menu Data
menu = [
    {'product_id': 'D001', 'product_name': 'Espresso', 'category': 'Beverage', 'price': 3.00, 'cost': 0.50},
    {'product_id': 'D002', 'product_name': 'Latte', 'category': 'Beverage', 'price': 4.50, 'cost': 1.20},
    {'product_id': 'D003', 'product_name': 'Cappuccino', 'category': 'Beverage', 'price': 4.50, 'cost': 1.10},
    {'product_id': 'D004', 'product_name': 'Americano', 'category': 'Beverage', 'price': 3.50, 'cost': 0.60},
    {'product_id': 'D005', 'product_name': 'Mocha', 'category': 'Beverage', 'price': 5.00, 'cost': 1.50},
    {'product_id': 'D006', 'product_name': 'Tea', 'category': 'Beverage', 'price': 3.00, 'cost': 0.30},
    {'product_id': 'F001', 'product_name': 'Croissant', 'category': 'Food', 'price': 3.50, 'cost': 1.00},
    {'product_id': 'F002', 'product_name': 'Muffin', 'category': 'Food', 'price': 3.00, 'cost': 0.80},
    {'product_id': 'F003', 'product_name': 'Bagel', 'category': 'Food', 'price': 2.50, 'cost': 0.70},
    {'product_id': 'F004', 'product_name': 'Sandwich', 'category': 'Food', 'price': 7.00, 'cost': 2.50},
    {'product_id': 'M001', 'product_name': 'Coffee Beans (1lb)', 'category': 'Merch', 'price': 15.00, 'cost': 8.00},
    {'product_id': 'M002', 'product_name': 'Mug', 'category': 'Merch', 'price': 12.00, 'cost': 5.00},
]

payment_methods = ['Cash', 'Credit Card', 'Mobile Payment']
stores = ['Downtown', 'Suburbs']

def generate_random_time(date):
    # Simulate business hours 7am - 8pm
    hour = np.random.choice(range(7, 20), p=[0.1, 0.2, 0.15, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.025, 0.025])
    minute = random.randint(0, 59)
    return date.replace(hour=hour, minute=minute)

data = []

current_date = START_DATE
while current_date <= END_DATE:
    # Daily transaction volume variation (weekend vs weekday)
    if current_date.weekday() >= 5: # Weekend
        daily_transactions = random.randint(150, 250)
    else:
        daily_transactions = random.randint(80, 150)
    
    for _ in range(daily_transactions):
        txn_date = generate_random_time(current_date)
        item = random.choice(menu)
        quantity = np.random.choice([1, 2, 3], p=[0.8, 0.15, 0.05])
        
        row = {
            'transaction_id': fake.uuid4(),
            'date': txn_date.date(),
            'time': txn_date.time(),
            'product_id': item['product_id'],
            'product_name': item['product_name'],
            'category': item['category'],
            'unit_price': item['price'],
            'quantity': quantity,
            'total_price': item['price'] * quantity,
            'payment_method': random.choice(payment_methods),
            'store_location': random.choice(stores)
        }
        data.append(row)
    
    current_date += timedelta(days=1)

df = pd.DataFrame(data)
df.to_csv('data/coffee_shop_sales.csv', index=False)
print(f"Dataset generated with {len(df)} records.")

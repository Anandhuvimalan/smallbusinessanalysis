import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set page configuration
st.set_page_config(
    page_title="Coffee Shop Sales Analysis",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to load data
@st.cache_data
def load_data():
    data_path = 'data/coffee_shop_sales.csv'
    if not os.path.exists(data_path):
        return None
    
    df = pd.read_csv(data_path)
    df['date'] = pd.to_datetime(df['date'])
    df['datetime'] = pd.to_datetime(df['date'].astype(str) + ' ' + df['time'].astype(str))
    df['month'] = df['date'].dt.to_period('M')
    df['hour'] = df['datetime'].dt.hour
    df['day_of_week'] = df['date'].dt.day_name()
    return df

# Load data
df = load_data()

if df is None:
    st.error("Data file not found. Please run `python generate_data.py` to generate the dataset first.")
    st.stop()

# --- Sidebar Filters ---
st.sidebar.title("Filters")
st.sidebar.markdown("Customize your view")

# Store Filter
stores = ['All'] + list(df['store_location'].unique())
selected_store = st.sidebar.selectbox("Select Store", stores)

# Category Filter
categories = ['All'] + list(df['category'].unique())
selected_category = st.sidebar.selectbox("Select Category", categories)

# Date Range Filter
min_date = df['date'].min()
max_date = df['date'].max()
start_date, end_date = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

# Apply Filters
filtered_df = df.copy()
filtered_df = filtered_df[(filtered_df['date'] >= pd.to_datetime(start_date)) & (filtered_df['date'] <= pd.to_datetime(end_date))]

if selected_store != 'All':
    filtered_df = filtered_df[filtered_df['store_location'] == selected_store]

if selected_category != 'All':
    filtered_df = filtered_df[filtered_df['category'] == selected_category]


# --- Main Dashboard ---
st.title("☕ Small Business Analysis: Coffee Shop")
st.markdown("Interactive dashboard for exploring sales data, trends, and product performance.")

# KPI Row
total_revenue = filtered_df['total_price'].sum()
total_txns = len(filtered_df)
avg_txn_value = filtered_df['total_price'].mean() if total_txns > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${total_revenue:,.2f}")
col2.metric("Total Transactions", f"{total_txns:,}")
col3.metric("Avg Transaction Value", f"${avg_txn_value:.2f}")

st.markdown("---")

# Layout: Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Product Analysis", "Hourly Patterns", "Raw Data"])

with tab1:
    st.subheader("Sales Overview")
    
    col_chart1, col_chart2 = st.columns(2)
    
    with col_chart1:
        st.markdown("**Monthly Sales Trend**")
        # Aggregate by month (convert period to string for plotting compatibility)
        monthly_sales = filtered_df.groupby('month')['total_price'].sum()
        monthly_sales.index = monthly_sales.index.astype(str)
        
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(monthly_sales.index, monthly_sales.values, marker='o', linestyle='-', color='b')
        ax.set_xlabel("Month")
        ax.set_ylabel("Revenue ($)")
        ax.grid(True)
        plt.xticks(rotation=45)
        st.pyplot(fig)

    with col_chart2:
        st.markdown("**Revenue by Store Location**")
        store_sales = filtered_df.groupby('store_location')['total_price'].sum()
        
        fig, ax = plt.subplots(figsize=(8, 5))
        sns.barplot(x=store_sales.index, y=store_sales.values, palette="coolwarm", ax=ax)
        ax.set_ylabel("Revenue ($)")
        st.pyplot(fig)

with tab2:
    st.subheader("Product Performance")
    
    col_prod1, col_prod2 = st.columns([2, 1])
    
    with col_prod1:
        st.markdown("**Top 5 Best Selling Products (Quantity)**")
        top_products = filtered_df.groupby('product_name')['quantity'].sum().sort_values(ascending=False).head(5)
        
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.barplot(x=top_products.values, y=top_products.index, palette="magma", ax=ax)
        ax.set_xlabel("Quantity Sold")
        st.pyplot(fig)
        
    with col_prod2:
        st.markdown("**Sales by Category**")
        category_sales = filtered_df.groupby('category')['total_price'].sum().sort_values(ascending=False)
        
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
        st.pyplot(fig)

with tab3:
    st.subheader("Operational Insights")
    st.markdown("**Peak Hours of Operation**")
    
    hourly_sales = filtered_df.groupby('hour')['total_price'].sum()
    
    fig, ax = plt.subplots(figsize=(12, 5))
    sns.barplot(x=hourly_sales.index, y=hourly_sales.values, palette="viridis", ax=ax)
    ax.set_xlabel("Hour of Day (24h)")
    ax.set_ylabel("Total Sales ($)")
    st.pyplot(fig)

with tab4:
    st.subheader("Raw Data View")
    st.markdown(f"Displaying {len(filtered_df)} records based on current filters.")
    st.dataframe(filtered_df.sort_values(by='datetime', ascending=False))

# Footer
st.markdown("---")
st.caption("Generated by Gemini CLI Agent")

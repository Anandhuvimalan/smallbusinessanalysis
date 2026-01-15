# Small Business Analysis - Coffee Shop Edition

This project simulates a year's worth of sales data for a small coffee shop business and performs a deep exploratory data analysis (EDA) to extract actionable business insights.

## 📂 Project Structure

```text
├── generate_data.py   # Script to generate synthetic sales dataset
├── analyze_data.py    # Script to analyze data and generate visualizations
├── data/
│   └── coffee_shop_sales.csv  # The generated dataset (created by generate_data.py)
├── analysis/          # Directory containing generated plots
│   ├── monthly_sales_trend.png
│   ├── hourly_sales.png
│   ├── category_distribution.png
│   ├── top_5_products.png
│   └── store_performance.png
└── README.md          # Project documentation
```

## 🚀 Features

*   **Data Generation:** Creates a realistic dataset including transaction IDs, dates, times, products, categories (Beverage, Food, Merch), costs, prices, payment methods, and store locations.
*   **Deep Analysis:**
    *   **Sales Trends:** Monthly revenue tracking to identify seasonal patterns.
    *   **Peak Hours:** Analysis of transaction volume by hour of the day.
    *   **Product Performance:** Identifies top-selling items and revenue contribution by category.
    *   **Store Comparison:** Compares performance between different store locations (e.g., Downtown vs. Suburbs).
*   **Visualizations:** Automatically generates and saves insightful charts using `matplotlib` and `seaborn`.

## 🛠️ Prerequisites

Ensure you have Python installed. You will need the following libraries:

*   pandas
*   numpy
*   matplotlib
*   seaborn
*   faker

## 📦 Installation

Install the required dependencies using pip:

```bash
pip install pandas numpy matplotlib seaborn faker
```

## 💻 Usage

### 1. Generate the Dataset
First, run the generation script to create the synthetic dataset. This will create a `data` folder and save `coffee_shop_sales.csv` inside it.

```bash
python generate_data.py
```

### 2. Run the Analysis
Once the data is generated, run the analysis script. This will process the CSV file, print an executive summary to the console, and save visualizations to the `analysis` folder.

```bash
python analyze_data.py
```

### 3. Run the Interactive Dashboard
Launch the Streamlit web application to explore the data interactively with filters for date, store, and category.

```bash
streamlit run app.py
```

## 📊 Sample Output (Executive Summary)

When you run the analysis, you will see a summary similar to this in your console:

```text
==============================
     EXECUTIVE SUMMARY     
==============================
Total Transactions: 50,700
Total Revenue: $350,715.00
Average Transaction Value: $6.92
Best Selling Category: Merch
Most Popular Product: Americano
Top Performing Store: Suburbs
==============================
Analysis complete. Visualizations saved to 'analysis/' directory.
```

## 📈 Visualizations

Check the `analysis/` directory for the following charts:
*   **monthly_sales_trend.png**: Revenue over time.
*   **hourly_sales.png**: Busiest hours of operation.
*   **category_distribution.png**: Sales split by product category.
*   **top_5_products.png**: Most popular items by quantity.
*   **store_performance.png**: Revenue comparison by location.

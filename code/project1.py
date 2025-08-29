# 1. Import Libraries
import pandas as pd
import os

# 2. Check current working directory
print("Current working directory:", os.getcwd())

# 3. Load Dataset
# Update the path below to the exact location of your 'sales_data.csv' file
file_path = r'C:\Users\Sinchal Shrivastava\OneDrive\Desktop\data analysis\sales_data.csv'

try:
    data = pd.read_csv(file_path)
    print("File loaded successfully!")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}. Please check the path and try again.")
    exit()

# 4. Initial Data Inspection
print("First 5 rows:")
print(data.head())
print("\nData Info:")
print(data.info())
print("\nMissing values per column:")
print(data.isnull().sum())

# 5. Data Cleaning
# Convert 'Date' to datetime
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Drop rows with missing values
data = data.dropna()

# Verify cleaning
print("\nData after cleaning:")
print(data.info())

# 6. Exploratory Data Analysis (EDA)
# Summary statistics
print("\nSummary statistics:")
print(data.describe())

# Total sales by product
product_sales = data.groupby('Product')['Sales'].sum().sort_values(ascending=False)
print("\nTotal sales by product:")
print(product_sales)

# Total sales by region
region_sales = data.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nTotal sales by region:")
print(region_sales)

# Monthly sales trend
data['YearMonth'] = data['Date'].dt.to_period('M')
monthly_sales = data.groupby('YearMonth')['Sales'].sum()

# 7. Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Plot monthly sales trend
plt.figure(figsize=(12,6))
monthly_sales.index = monthly_sales.index.to_timestamp()
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.tight_layout()
plt.show()

# Bar chart: Sales by Product
plt.figure(figsize=(10,5))
product_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Product')
plt.xlabel('Product')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Bar chart: Sales by Region
plt.figure(figsize=(8,4))
region_sales.plot(kind='bar', color='salmon')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Correlation heatmap (only numeric columns)
plt.figure(figsize=(6,4))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.show()

# 8. Insights and Recommendations
print("""
Insights:
- Peak sales months can be identified from the monthly sales trend plot.
- Best-selling products and regions are visible from bar charts.
- Correlation heatmap shows relationships between numeric variables.

Recommendations:
- Focus marketing efforts on best-selling products and regions.
- Investigate low sales periods to identify causes and improve.
- Use correlation insights to explore factors influencing sales.
""")

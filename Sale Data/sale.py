import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv('Sale Data/sales_100k.csv')

# ----- Data Overview -----
print(f"Initial Info:\n{df.info()}")
print("\nDescriptive Statistics:\n", df.describe())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values (Before Filling):\n", df.isnull().sum())

# ----- Handle Missing Values -----
df['Sales_Amount'] = df['Sales_Amount'].fillna(df['Sales_Amount'].mean())
df['Discount'] = df['Discount'].fillna(df['Discount'].median())
df['Customer_Age'] = df['Customer_Age'].fillna(df['Customer_Age'].mean())
df['Customer_Gender'] = df['Customer_Gender'].fillna(np.random.choice(['Male', 'Female']))
df.loc[df['Customer_Gender'] == 'Other', 'Customer_Gender'] = np.random.choice(['Male', 'Female'])

print("\nMissing Values (After Filling):\n", df.isnull().sum())

# ----- Check for Duplicates -----
print(f"\nNumber of Duplicates: {df.duplicated().sum()}")

# ============================================
# ✅ Task 1: Total Sales, Missing, Outliers
# ============================================
print(f"\n✅ Total Sales: {df['Sales_Amount'].sum():.2f} $")

# Missing already handled above
Q1 = df['Sales_Amount'].quantile(0.25)
Q3 = df['Sales_Amount'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['Sales_Amount'] < Q1 - 1.5 * IQR) | (df['Sales_Amount'] > Q3 + 1.5 * IQR)]
print(f"Number of Outliers in Sales_Amount: {len(outliers)}")

# ============================================
# ✅ Task 2: Revenue Trends Over Time
# ============================================
df['Date_of_Sale'] = pd.to_datetime(df['Date_of_Sale'])
df['Sale_Month'] = df['Date_of_Sale'].dt.to_period('M')
df['Sale_Week'] = df['Date_of_Sale'].dt.isocalendar().week

monthly_sales = df.groupby('Sale_Month')['Sales_Amount'].sum()
weekly_sales = df.groupby('Sale_Week')['Sales_Amount'].sum()

print("\nMonthly Sales (Last 5 Months):\n", monthly_sales.tail())
print("\nWeekly Sales:\n", weekly_sales)

# ============================================
# ✅ Task 3: Most Revenue by Product Category
# ============================================
most_revenue = df.groupby('Product_Category')['Sales_Amount'].sum().sort_values(ascending=False)
print("\nRevenue by Product Category:\n", most_revenue)

# ============================================
# ✅ Task 4: High vs Low Performers
# ============================================
top_sales = most_revenue.idxmax()
top_value = most_revenue.max()
least_sales = most_revenue.idxmin()
least_value = most_revenue.min()

print(f"\nTop Performer: {top_sales} (${top_value:.2f})")
print(f"Low Performer: {least_sales} (${least_value:.2f})")

# ============================================
# ✅ Task 5: Product Performance Over Time(Monthly and Weekly)
# ============================================
performance_monthly = df.groupby(['Product_Category', 'Sale_Month'])['Sales_Amount'].sum().reset_index()
performance_weekly = df.groupby(['Product_Category', 'Sale_Week'])['Sales_Amount'].sum().reset_index()

print("\nProduct Performance by Month:\n", performance_monthly.head())
print("\nProduct Performance by Week:\n", performance_weekly.head())

# ============================================
# ✅ Task 6: Demographics ( Which gender brings in more revenue? which age group buys more? Which 5 cities perform best?)
# ============================================
revenue_by_gender = df.groupby('Customer_Gender')['Sales_Amount'].sum().sort_values(ascending=False)
print("\nRevenue by Gender:\n", revenue_by_gender)

# Age Group Buckets
bins = [0, 18, 25, 35, 50, 65, 100]
labels = ['Teen', 'Youth', 'Young Adult', 'Adult', 'Senior', 'Elder']
df['Age_Group'] = pd.cut(df['Customer_Age'], bins=bins, labels=labels)

revenue_by_age = df.groupby('Age_Group')['Sales_Amount'].sum().sort_values(ascending=False)
print("\nRevenue by Age Group:\n", revenue_by_age)

top_cities = df.groupby('Sales_Region')['Sales_Amount'].sum().sort_values(ascending=False)
print("\nTop 5 Sales Regions:\n", top_cities.head())

# ============================================
# ✅ Task 7: Customer Behavior(Most Frequently Purchased Products, Average Purchase Amount Per Order)
# ============================================
most_sold_item = df['Product_Category'].value_counts().sort_values(ascending=False)
average_purchase = df['Sales_Amount'].mean()

print("\nMost Frequently Purchased Products:\n", most_sold_item)
print(f"\nAverage Purchase Amount per Order: {average_purchase:.2f} $")

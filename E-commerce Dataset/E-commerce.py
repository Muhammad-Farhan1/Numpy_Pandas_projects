# Import libraries
import pandas as pd
import matplotlib.pyplot as plt

# Loading Data
df = pd.read_csv("Pakistan Largest Ecommerce Dataset.csv" , low_memory=False)

# Displaying first 5 rows
#print(df.head())

# Inspecting the column names and data types
#print(df.dtypes)

# Summary of data
#print(df.describe())

# Total number of Rows
#print(f"Total : {len(df)}")

# Checking for duplicate records
#print(f"Duplicate records: {df[df.duplicated()].sum()}")


#1. Calculate total grand_total, total item_id (orders), and average order value.
Total_Amount = df['grand_total'].sum()
Total_orders = df['item_id'].nunique() 
#nunique() in Pandas is used to count the number of unique (distinct) values in a column.
Avg_Order = Total_Amount / Total_orders
#print(f"The average of orders : {Avg_Order:.2f}")


#2.Group by Year & Month, plot line chart of sales.
df['Working Date'] = pd.to_datetime(df['Working Date'])
df['Working Date'] = df['Working Date'].ffill()
#print(df['Working Date'].isnull().sum())

#---Monthly Trend
df['Monthly_Sales'] = df['Working Date'].dt.to_period('M')
Monthy_Trend = df.groupby('Monthly_Sales')['grand_total'].sum()
#print(Monthy_Trend)

#------------ Graph ------------
plt.figure(figsize=(12,8))
plt.plot(Monthy_Trend.index.astype(str) , Monthy_Trend.values , marker='o')
plt.title("Monthly Revenue Trend")
plt.xlabel('Months')
plt.ylabel('Total Sale')
plt.xticks(rotation=45)
plt.tight_layout()


#---Yearly Trend
df['Yearly_Sales'] = df['Working Date'].dt.to_period('Y')
Yearly_Trend = df.groupby('Yearly_Sales')['grand_total'].sum()
#print(Yearly_Trend)

#------------ Graph ------------
plt.figure(figsize=(12,8))
plt.plot(Yearly_Trend.index.astype(str) , Yearly_Trend.values , marker='o')
plt.title("Yearly Revenue Trend")
plt.xlabel('Years')
plt.ylabel('Total Sale')

#3.Daily Sales Pattern → Group by Working Date

Daily_Sale = df.groupby('Working Date')['grand_total'].sum()
Daily_Sale = Daily_Sale.rolling(window=7).mean()   # 7-day rolling average

#------------ Graph ------------
plt.figure(figsize=(12,8))
plt.plot(Daily_Sale.index, Daily_Sale.values, marker='o' , color='Red')
plt.title("Daily Revenue Trend (7-Day Avg)")
plt.xlabel("Date")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()


#4.Revenue by Category → Compare sales across category_name_1 with bar chart.
df['category_name_1'] = df['category_name_1'].replace('\\N' , 'News')
df['category_name_1'] = df['category_name_1'].ffill()
Revenue_By_Category = df.groupby('category_name_1')['grand_total'].sum()
#print(Revenue_By_Category)

#------------ Graph ------------
plt.figure(figsize=(12,8))
Revenue_By_Category.plot(kind='bar', color = 'orange', edgecolor = 'blue')
plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.xticks(rotation=90)
plt.tight_layout()


#5.Top 10 Products → Use sku to find best-selling products by revenue & quantity.
#---by Revenue
df['sku'] = df['sku'].ffill()
Best_Selling_Revenue = df.groupby('sku')['grand_total'].sum().sort_values(ascending=False)
#print(Best_Selling_Revenue.head(10))

#---by Quantity
Best_Selling_Quantity = df.groupby('sku')['item_id'].count().sort_values(ascending=False)
#print(Best_Selling_Quantity.head(10))


#6.Unique Orders Growth
Monthly_Growth = df.groupby('Monthly_Sales')['item_id'].nunique()
#print(Monthly_Growth)


#7. New vs Returning Customers
df['Working Date'] = pd.to_datetime(df['Working Date'])
df['Customer Since'] = pd.to_datetime(df['Customer Since'])

df['Customer_Type'] = (df['Working Date'].dt.to_period('M') == df['Customer Since'].dt.to_period('M'))
df['Customer_Type'] = df['Customer_Type'].map({True : "New" , False : "Returning"})
df['Month'] = df['Working Date'].dt.to_period('M')
New_vs_return = df.groupby(['Month', 'Customer_Type'])['item_id'].nunique().unstack().fillna(0)
#print(New_vs_return)


#8.Customer Lifetime Value (CLV) → Avg revenue per customer.
Avg_revenue_per_customer = df.groupby('Customer ID')['grand_total'].mean().mean()
'''
➡️First .mean() → average revenue per customer.
➡️ Second .mean() → average of those customer averages = overall CLV
'''
#print(Avg_revenue_per_customer)


#9.Top 10 Customers (VIPs) → Customers contributing highest revenue.
highest_Revenue = df.groupby('Customer ID')['grand_total'].agg(['sum','count']).sort_values(by='sum', ascending=False)
#print(highest_Revenue.head(10))


#10.Customer Growth Trend → New customers added each month (line chart).
df['Monthly_Customers'] = df['Working Date'].dt.to_period("M")
first_purchase = df.groupby('Customer ID')['Monthly_Customers'].min()
New_Customers = first_purchase.value_counts().sort_index()

#------------ Graph ------------
plt.figure(figsize=(12,8))  
plt.plot(New_Customers.index.astype(str), New_Customers.values, marker='o', color='blue', label='New Customers')
plt.title('New Customers Each Month')
plt.xlabel('Months')
plt.ylabel('New Customers')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()


#11.Order Status Distribution →Pie chart of status (Complete, Pending, Refunded)

order_status = df.groupby('status')['item_id'].count()

plt.figure(figsize=(12,8))
plt.pie(order_status, autopct='%1.1f%%')
plt.tight_layout()
plt.show()  




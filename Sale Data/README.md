# 🛒 Store Sales Analysis (sales_100k.csv)

This project analyzes a store sales dataset of 100,000 records using Python and libraries such as **Pandas**, **NumPy**, and **Matplotlib**. It includes data cleaning, exploratory analysis, and revenue-based insights across products, customers, and time.

---

## 📁 Dataset
- File: `sales_100k.csv`
- Fields include:
  - `Date_of_Sale`
  - `Product_Category`
  - `Sales_Amount`
  - `Discount`
  - `Customer_Gender`
  - `Customer_Age`
  - `Sales_Region`

---

## ✅ Tasks Performed

### 🔹 Task 1: Total Sales, Missing Values, and Outlier Detection
- Filled missing values using mean, median, and random sampling.
- Replaced `Other` gender values with `Male` or `Female`.
- Detected outliers in `Sales_Amount` using the IQR method.
- Calculated total sales in USD.

### 🔹 Task 2: Revenue Trends Over Time
- Converted `Date_of_Sale` to datetime format.
- Extracted and grouped sales data monthly and weekly to identify trends.

### 🔹 Task 3: Product Categories Generating Most Revenue
- Aggregated total revenue by `Product_Category`.
- Identified the most and least profitable categories.

### 🔹 Task 4: High vs Low Performing Products
- Highlighted top-performing and underperforming product categories.

### 🔹 Task 5: Product Performance Over Time
- Tracked category-wise sales over months and weeks.

### 🔹 Task 6: Customer Demographics Analysis
- Analyzed total sales by gender.
- Binned customers into age groups.
- Identified top-performing cities by revenue.

### 🔹 Task 7: Customer Behavior Insights
- Found most frequently purchased product categories.
- Calculated average purchase amount per order.

---

## 📊 Upcoming: Data Visualization Tasks
I will visualize:
1. Monthly revenue trend
2. Top 5 product categories
3. Sales by customer age group
4. Revenue by gender
5. Weekly sales trend

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib

---

## 💡 Author
**Muhammad Farhan**  
Aspiring Python Developer and ML Engineer  
📍 Pakistan

---

## 🌐 License
This project is open for learning and contribution.


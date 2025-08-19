# House Price Analysis Project

This project performs a comprehensive exploratory data analysis (EDA) on the King County House Sales dataset (`kc_house_data.csv`). The dataset contains house sale prices for King County, including Seattle, USA.

## 📁 Dataset Used
- kc_house_data.csv

## 🔧 Libraries Used
- pandas
- matplotlib.pyplot

## 🔍 Key Steps Performed

1. **Data Loading and Inspection**
   - Loaded data using pandas
   - Checked for null values and data types
   - Converted `date` to datetime format

2. **Data Cleaning & Feature Engineering**
   - Removed outliers from `bedrooms` column using IQR method
   - Renamed columns for better readability
   - Extracted `year` and `month` from `date`

3. **Exploratory Data Analysis (EDA)**
   - Top 10 most expensive houses
   - Average house price by number of bedrooms
   - ZIP code with the highest average house prices
   - Correlation of other features with `price`
   - Price trend over time by `year`
   - Price comparison for houses with and without `waterfront`
   - Count and average price of houses by `condition`
   - Average price by construction `grade`
   - Impact of `view` rating on price
   - Distribution of number of `floors`
   - Top 5 ZIP codes with the most house sales

4. **Data Visualization**
   - Histogram of house prices
   - Scatter plot of `sqft_living` vs `price`

5. **Output**
   - Cleaned dataset saved as `kc_house_data_cleaned.csv`
   - Visualizations saved as PNG images

## 📄 Files Generated
- kc_house_data_cleaned.csv – cleaned dataset
- Plot_Of_Prices.png – histogram plot
- Relation_Price_Area.png – scatter plot

## ✅ Status
This analysis is complete and saved as both code and visuals. It can be further extended for predictive modeling or dashboard creation.

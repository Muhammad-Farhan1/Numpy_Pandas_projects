import pandas as pd
import matplotlib.pyplot as plt

#====================
# Read and Inspect Data
#====================

df = pd.read_csv('House Data\\kc_house_data.csv')

# Check information of Data
print("Info of Data:")
print(df.info())

# Check descriptive statistics
print("\nSummary Statistics:")
print(df.describe())

#========================================
# 1. Check for null values in the dataset
#========================================
print("\nNull Values in Each Column:")
print(df.isnull().sum())  # No nulls expected

#===========================================
# 2. Convert date column to datetime format
#===========================================
df['date'] = pd.to_datetime(df['date'])

#==================================================
# 3. Rename columns for clarity (replace underscores)
#==================================================
df.rename(columns={
    'sqft_living': 'sqft living',
    'sqft_lot': 'sqft lot',
    'sqft_above': 'sqft above',
    'sqft_basement': 'sqft basement',
    'yr_built': 'yr built',
    'yr_renovated': 'yr renovated',
    'sqft_living15': 'sqft living15',
    'sqft_lot15': 'sqft lot15'
}, inplace=True)

#===================================
# 4. Extract year and month from date
#===================================
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

#===============================================
# 5. Top 10 most expensive houses with details
#===============================================
Expensive_House = df.sort_values(by='price', ascending=False)
print("\nTop 10 Most Expensive Houses:")
print(Expensive_House.head(10))

#===================================================
# 6. Average house price by bedrooms (after filtering)
#===================================================
Q1 = df['bedrooms'].quantile(0.25)
Q3 = df['bedrooms'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['bedrooms'] >= 1) & (df['bedrooms'] <= 11)]

average_price_bedrooms = df.groupby('bedrooms')['price'].mean()
print("\nAverage House Price by Bedrooms:")
print(average_price_bedrooms)

#======================================================
# 7. ZIP code with the highest average house prices
#======================================================
high_Price_ZIP = df.groupby('zipcode')['price'].mean()
print("\nZIP Code with Highest Average Price:")
print("ZIP Code:", high_Price_ZIP.idxmax())
print("Price:", high_Price_ZIP.max())

#======================================================
# 8. Most strongly correlated features with house price
#======================================================
correlation = df.corr()
price_corr = correlation['price'].sort_values(ascending=False)
print("\nCorrelation with House Price:")
print(price_corr)

#===============================================
# 9. Distribution plot of prices using histogram
#===============================================
plt.figure(figsize=(10, 5))
plt.hist(df['price'], bins=30, color='lightpink', edgecolor='white')
plt.ylabel('Frequency')
plt.xlabel('House Prices')
plt.title('Distribution of House Prices')
plt.grid(True)
#plt.savefig('Plot_Of_Prices.png', dpi=300, bbox_inches='tight')
plt.show()

#=======================================================
# 10. Scatter plot: sqft_living vs price to explore trend
#=======================================================
plt.figure(figsize=(10, 5))
plt.scatter(df['sqft living'], df['price'], color='brown', marker='o', alpha=0.5)
plt.title('Relationship Between House Price and Living Area')
plt.xlabel('Square Footage of Living Area')
plt.ylabel('House Price')
plt.grid(True)
#plt.savefig('Relation_Price_Area.png', dpi=300, bbox_inches='tight')
plt.show()

#===================================
# 11. Analyze house prices over time
#===================================
analyze_price = df.groupby('year')['price'].mean()
print("\nAverage House Prices Over the Years:")
print(analyze_price)

#=====================================================
# 12. Average price comparison of houses with waterfront
#=====================================================
with_waterfront = df.groupby('waterfront')['price'].mean()
print("\nAverage Price: Waterfront vs Non-Waterfront:")
print(with_waterfront)

#=====================================================
# 13. Count of houses by condition and their average price
#=====================================================
houses_by_cond_Price = df.groupby('condition')['price'].agg(['count', 'mean'])
print("\nHouse Count and Average Price by Condition:")
print(houses_by_cond_Price)

#=======================================
# 14. Average price by construction grade
#=======================================
avg_price_by_grade = df.groupby('grade')['price'].agg(['mean'])
print("\nAverage Price by Construction Grade:")
print(avg_price_by_grade)

#=======================================
# 15. Analyze the impact of view on price
#=======================================
impact_view_on_price = df.groupby('view')['price'].agg(['mean'])
print("\nAverage Price by View Quality:")
print(impact_view_on_price)

#======================================================
# 16. Distribution of number of floors across all houses
#======================================================
no_of_floor_Houses = df['floors'].value_counts().sort_index()
print("\nNumber of Houses by Floors:")
print(no_of_floor_Houses)

#======================================================
# 17. Top 5 ZIP codes with the most houses sold
#======================================================
five_Zipcode = df['zipcode'].value_counts()
print("\nTop 5 ZIP Codes with Most Houses Sold:")
print(five_Zipcode.head())

#====================
# Save the cleaned dataset
#====================
df.to_csv('House Data\\kc_house_data_cleaned.csv', index=False)
print("\n✅ Cleaned dataset saved as 'kc_house_data_cleaned.csv'")


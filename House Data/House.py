import pandas as pd
import matplotlib.pyplot as plt

#Read Data
df = pd.read_csv('House Data\\kc_house_data.csv')

#Check information of Data
#print(f"Info of Data: {df.info()}")

#Check mean,count,min,max and %
#print(df.describe())

#========================================
# 1. Check for null values in the dataset
#========================================
#print(df.isnull().sum())

#No Null value in dataset

#===============================================
# 2. Check data types of all columns and convert
#===============================================

#print(df.dtypes)
df['date'] = pd.to_datetime(df['date'])

#==========================================================
# 3. Rename column headers for clarity (replace underscores)
#==========================================================

#print(f"Before Renaming: {df.columns}")
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

#Other Method: 
#df.columns = df.columns.str.replace('_', ' ')
#print(f"After Rename:{df.columns}")

#-----------------📊 Exploratory Data Analysis (EDA)------------------

#===================================
# 4.  Extract year, month From Date
#===================================

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

#===================================
# 5.Top 10 most expensive houses with details
#===================================

Expensive_House = df[df.columns].sort_values(by=['price'] , ascending=False)
#print(Expensive_House.head(10))

#===================================
# 6. Average house price by bedrooms
#===================================

#Outlier of 0 and 33 Came let solve out it first using IQR method--
Q1 = df['bedrooms'].quantile(0.25)
Q3 = df['bedrooms'].quantile(0.75)
IQR = Q3 - Q1
df = df[(df['bedrooms'] >= 1) & (df['bedrooms'] <= 11)]

average_price_bedrooms = df.groupby('bedrooms')['price'].mean()
#print(average_price_bedrooms)

#======================================================
# 7.Which ZIP code has the highest average house prices
#======================================================
high_Price_ZIP = df.groupby('zipcode')['price'].mean()
#print(high_Price_ZIP.idxmax())
#print(high_Price_ZIP.max())


#======================================================
# 8.Find  Most Strongly Correlated with House Price
#======================================================
correlation = df.corr()
price_corr = correlation['price'].sort_values(ascending=False)
#print(price_corr)

#===============================================
#9. Distribution plot of prices using histogram
#===============================================
plt.hist(df['price'], bins=30, color='lightpink', edgecolor='white')
plt.ylabel('Frequency')
plt.xlabel('House Prices')
plt.title('Distribution of House Prices')
plt.grid(True)
plt.savefig('Plot_Of_Prices.png' , dpi=300 , bbox_inches='tight')





'''
 or KDE
Scatter plot: sqft_living vs price to explore trend
Boxplot of price by number of bedrooms
Analyze house prices over time (if date column exists)
Average price comparison of houses with and without waterfront
Count of houses by condition and their average price
Average price by construction grade
Analyze the impact of view on price
Distribution of number of floors across all houses
Top 5 ZIP codes with the most houses sold

🧠 Insights & Feature Engineering
Create new feature like house_age = current_year - yr_built, analyze its relation with price
Compare average price of houses built before 2000 vs after 2000


'''
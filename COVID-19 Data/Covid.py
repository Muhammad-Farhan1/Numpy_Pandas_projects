import pandas as pd

#Loading data through CSV file
df = pd.read_csv("COVID-19 Data\\vaccinations.csv")

#Read first 5 rows
#print(df.head())

# Inspecting the column names and data types
#print(df.dtypes)

#Info of Data
#print(df.info())

#Mean, Max, Min , Std etc
#print(df.describe())

#Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])
#print(df['date'])
#Before it was an object but now its datetime, DataType changed!

#Check duplicate rows
#print(df.duplicated().sum())
#this dataset hasn't any duplication but in order to remove duplicate rows use this
# print(df.drop_duplicates())

#Handling Missing Values
#print(df.isnull().sum())

#Filling all values
df['total_vaccinations'] = df['total_vaccinations'].fillna(df['total_vaccinations'].mean())
df['people_vaccinated'] = df['people_vaccinated'].fillna(df['people_vaccinated'].median())
df['people_fully_vaccinated'] = df['people_fully_vaccinated'].fillna(df['people_fully_vaccinated'].median())
df['total_boosters'] = df['total_boosters'].fillna(df['total_boosters'].mean())
df['daily_vaccinations_raw'] = df['daily_vaccinations_raw'].fillna(df['daily_vaccinations_raw'].median())
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(df['daily_vaccinations'].mean())
df['total_vaccinations_per_hundred'] = df['total_vaccinations_per_hundred'].fillna(df['total_vaccinations_per_hundred'].median())
df['people_vaccinated_per_hundred'] = df['people_vaccinated_per_hundred'].fillna(df['people_vaccinated_per_hundred'].median())
df['people_fully_vaccinated_per_hundred'] = df['people_fully_vaccinated_per_hundred'].fillna(df['people_fully_vaccinated_per_hundred'].mean())
df['total_boosters_per_hundred'] = df['total_boosters_per_hundred'].fillna(df['total_boosters_per_hundred'].mean())
df['daily_vaccinations_per_million'] = df['daily_vaccinations_per_million'].fillna(df['daily_vaccinations_per_million'].mean())

#No  more Null values
#print(df.isnull().sum())

#top 10 countries with the highest number of fully vaccinated people
fully_vacinated = df.sort_values('people_fully_vaccinated', ascending=False)
#print(fully_vacinated.head(10))

# first date when each country started vaccinating
started_vax = df[df['total_vaccinations'] > 0]
first_date = started_vax.groupby('location')['date'].min()
print(first_date)
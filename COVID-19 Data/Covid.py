import pandas as pd

# Load data from CSV file
df = pd.read_csv("COVID-19 Data\\vaccinations.csv")

# Display first 5 rows
print(df.head())

# Inspect column names and data types
print(df.dtypes)

# General information about the dataset
print(df.info())

# Statistical summary
print(df.describe())

# Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])
print(df['date'])  # Confirm conversion

# Check and display the number of duplicate rows
print("Duplicate Rows:", df.duplicated().sum())

# Remove duplicate rows (if any)
df = df.drop_duplicates()

# Handling Missing Values
print("Missing Values Before Filling:")
print(df.isnull().sum())

# Fill missing values appropriately
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

# Confirm all missing values are handled
print("Missing Values After Filling:")
print(df.isnull().sum())

# Top 10 countries with the highest number of fully vaccinated people
fully_vaccinated = df.sort_values('people_fully_vaccinated', ascending=False)
print("Top 10 Countries by Fully Vaccinated People:")
print(fully_vaccinated.head(10))

# First date when each country started vaccinating
started_vax = df[df['total_vaccinations'] > 0]
first_date = started_vax.groupby('location')['date'].min()
print("First Vaccination Date for Each Country:")
print(first_date)

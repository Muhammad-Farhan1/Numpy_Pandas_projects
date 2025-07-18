import pandas as pd
import numpy as np

#Read data from csv file 
df = pd.read_csv("Banking system\messed_data.csv")

#Handling the missing values:
print("Missing Values:")
print(df.isnull().sum()) 

#Fill the missing values:
df['Age'] = df["Age"].fillna(df["Age"].mean())
df['Experience'] = df["Experience"].fillna(df["Experience"].median())
df['Salary'] = df["Salary"].fillna(df["Salary"].mean())
df['Rating'] = df["Rating"].fillna(df["Rating"].mean())


#replace the infinte values with NaN
df.replace([np.inf , -np.inf], np.nan, inplace=True)

#Find the average
numeric_cols = df.select_dtypes(include=[np.number]).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

#No missing values
print("\nMissing Values After Handling:")
print(df.isnull().sum())

#For View Data on terimal 
print(df)

#Now save the cleaned data
df.to_csv("Cleaned_Data.csv" , index=False)
print("Saves the cleaned data as 'Cleaned_Data.csv'")
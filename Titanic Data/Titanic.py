import pandas as pd

#Reading Dataset
df = pd.read_csv("Titanic Data\Titanic-Dataset.csv")

#Checking Null Values
#print(df.isnull().sum())

#Filling Null Value
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])
df['Embarked'] = df['Embarked'].fillna('U')

#All values filled
#print(df.isnull().sum())

#Convert 'male or female' to '0 or 1'
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}) 
#Convert 'S,C,Q' to '10,20,30'
df['Embarked'] = df['Embarked'].map({"S":10, "C":20, "Q":30})
print(df['Embarked'])
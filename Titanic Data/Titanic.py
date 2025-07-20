#Tasks are written with numbers (1,2,3 etc)

import pandas as pd
#1: Load and View the Data
#Reading Dataset
df = pd.read_csv("Titanic Data\Titanic-Dataset.csv")

#Checking Null Values
#print(df.isnull().sum())

#2: Data Cleaning Tasks

#Filling Null Value
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0])
df['Embarked'] = df['Embarked'].fillna('U')

#All values filled
#print(df.isnull().sum())

#3:Convert Sex and Embarked into numeric value

#Convert 'male or female' to '0 or 1'
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}) 
#Convert 'S,C,Q' to '10,20,30'
df['Embarked'] = df['Embarked'].map({"S":10, "C":20, "Q":30})

#4:How many male vs female passengers survived

survivors_by_sex = df[df['Survived'] == 1]['Sex'].value_counts()
#print(survivors_by_sex)

#5: What is the survival rate by Pclass
survival_Pclass = df.groupby('Pclass')['Survived'].mean() * 100
#print(survival_Pclass)

#6: What is the average age of survivors vs non-survivors
survival_age = df.groupby('Survived')['Age'].mean()
print(survival_age)
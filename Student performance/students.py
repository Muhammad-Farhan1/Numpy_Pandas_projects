import pandas as pd
import numpy as np 

#Read data from dataset:
df = pd.read_csv("Student performance\StudentPerformanceFactors.csv")

#Displaying first 15 rows:
#print(df.head(15))

#Inspecting the column name and its data type:
#print(df.dtypes)

#Summary of data:
#print(df.describe())

#Total students:
#print(f"Total students: , {len(df)}")

#Checking Duplications:
#print(df[df.duplicated()].sum())

#Checking for null values:
#print(df.isnull().sum())

#Filling values randomly with 'low', 'medium', or 'high':
df['Teacher_Quality'] = df['Teacher_Quality'].fillna(np.random.choice(['Low', 'Medium', 'High']))

#fill missing values based on most frequent value:
frequent_values = df['Parental_Education_Level'].mode()[0]
df['Parental_Education_Level'] = df['Parental_Education_Level'].fillna(frequent_values)

#fill missing values based on most frequent value:
distane = df['Distance_from_Home'].mode()[0]
df['Distance_from_Home'] = df['Distance_from_Home'].fillna(distane)

#All values filled:
#print(df.isnull().sum()) -> 0 😀

#List unique values in 'Gender' & 'Exam_Score'
#print(df['Gender'].unique())
#print(df['Exam_Score'].unique())

#Counting Values:
#print(df['Distance_from_Home'].value_counts(dropna=False)) 
# dropna=False is useful when you want to also count missing values.


#Detect outliers in 'Exam_Score' or 'Attendance' (e.g., >100 or <0)
outliers_score = df[(df['Exam_Score'] > 100) | (df['Exam_Score'] < 0)] #Detect 
score_mean = df[(df['Exam_Score'] >= 0) & (df['Exam_Score'] <= 100)]['Exam_Score'].mean() #Calculate mean of valid scores
df.loc[(df['Exam_Score'] < 0) | (df['Exam_Score'] > 100), 'Exam_Score'] = int(score_mean) #Replace outliers with the mean
#print(score_mean)

outliers_Attandence = df[(df['Attendance'] > 100) | (df['Attendance'] < 0)]
#No outlier exists 

#students scored above 90
no_of_stds = df[(df['Exam_Score'] > 90)]
print(f"Number of students who got more than 90 marks are :{len(no_of_stds)}")

#Students who passed but had attendance below 60
check_std = df[(df['Attendance'] < 60) & (df['Extracurricular_Activities'] == 'Yes')]
print(len(check_std))

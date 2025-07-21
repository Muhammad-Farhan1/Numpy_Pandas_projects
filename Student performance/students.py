import pandas as pd
import numpy as np 

# Read data from dataset
df = pd.read_csv(r"Student performance\StudentPerformanceFactors.csv")

# Displaying first 15 rows
print(df.head())

# Inspecting the column names and data types
print(df.dtypes)

# Summary of data
print(df.describe())

# Total number of students
print(f"Total students: {len(df)}")

# Checking for duplicate records
print(f"Duplicate records: {df.duplicated().sum()}")

# Checking for null values before filling values
print(df.isnull().sum())

# Fill missing values in 'Teacher_Quality' randomly with 'Low', 'Medium', or 'High'
df['Teacher_Quality'] = df['Teacher_Quality'].fillna(np.random.choice(['Low', 'Medium', 'High']))

# Fill missing values in 'Parental_Education_Level' with most frequent value
frequent_value = df['Parental_Education_Level'].mode()[0]
df['Parental_Education_Level'] = df['Parental_Education_Level'].fillna(frequent_value)

# Fill missing values in 'Distance_from_Home' with most frequent value
most_common_distance = df['Distance_from_Home'].mode()[0]
df['Distance_from_Home'] = df['Distance_from_Home'].fillna(most_common_distance)

# Fill missing values in 'Hours_Studied' with the mean
df['Hours_Studied'] = df['Hours_Studied'].fillna(df['Hours_Studied'].mean())

# All values filled check
print(df.isnull().sum())

# Unique values in 'Gender' and 'Exam_Score'
print(df['Gender'].unique())
print(df['Exam_Score'].unique())

# Value counts for 'Distance_from_Home' (including NaN)
print(df['Distance_from_Home'].value_counts(dropna=False))

# Detect and fix outliers in 'Exam_Score'
outliers_score = df[(df['Exam_Score'] > 100) | (df['Exam_Score'] < 0)]
score_mean = df[(df['Exam_Score'] >= 0) & (df['Exam_Score'] <= 100)]['Exam_Score'].mean()
df.loc[(df['Exam_Score'] < 0) | (df['Exam_Score'] > 100), 'Exam_Score'] = int(score_mean)
print(f"Replaced outlier scores with mean: {int(score_mean)}")

# Detect outliers in 'Attendance' (just for review)
outliers_attendance = df[(df['Attendance'] > 100) | (df['Attendance'] < 0)]
print(f"Outliers in Attendance: {len(outliers_attendance)}")

# Students who scored above 90
high_scorers = df[df['Exam_Score'] > 90]
print(f"Number of students who got more than 90 marks: {len(high_scorers)}")

# Students who passed but had attendance below 60 and did extracurricular activities
low_attendance = df[(df['Attendance'] < 60) & (df['Extracurricular_Activities'] == 'Yes')]
print(f"Students with less than 60% attendance but participated in extracurricular: {len(low_attendance)}")

# Average Exam Score by Hours Studied
average_exam_by_hours = df.groupby('Hours_Studied')['Exam_Score'].mean()
print(average_exam_by_hours)

# Average Attendance by Gender
average_attendance = df.groupby('Gender')['Attendance'].mean()
print(average_attendance)

# Average exam scores between students who participate in extracurricular activities
average_score_by_activity = df.groupby("Extracurricular_Activities")['Exam_Score'].mean()
print(average_score_by_activity)

# Compare average hours studied between different parental education levels
average_hours_by_education = df.groupby('Parental_Education_Level')['Hours_Studied'].mean()
print(average_hours_by_education)

# Top 10 students with the highest scores
top_students = df.sort_values(by='Exam_Score', ascending=False)
print(top_students.head(10))

# List students who scored between 40 and 60
students_between_40_60 = df[(df['Exam_Score'] >= 40) & (df['Exam_Score'] <= 60)]
print(students_between_40_60)

# Compare average scores of male vs female students
avg_score_by_gender = df.groupby('Gender')['Exam_Score'].mean()
print(avg_score_by_gender)

# Most common parental education level
common_edu_level = df['Parental_Education_Level'].value_counts()
print(common_edu_level)

# Explore correlation between Score and Attendance
score_attendance_corr = df['Exam_Score'].corr(df['Attendance'])
print(f"Correlation between Exam Score and Attendance: {score_attendance_corr}")

# Save cleaned data
df.to_csv('Cleaned_Student_Performance.csv', index=False)
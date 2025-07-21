This project involves cleaning, analyzing, and drawing insights from a student performance dataset. It covers data preprocessing, handling missing values and outliers, and exploring key metrics using Pandas.

📂 Dataset Used
File: StudentPerformanceFactors.csv
Rows: ~30
Columns include:

Gender

Exam_Score

Attendance

Hours_Studied

Parental_Education_Level

Teacher_Quality

Distance_from_Home

Extracurricular_Activities

🧹 Data Cleaning Steps
Loaded dataset using pandas.read_csv()

Checked for duplicates

Filled missing values:

Teacher_Quality: Randomly with 'Low', 'Medium', or 'High'

Parental_Education_Level: With most frequent value

Distance_from_Home: With mode

Hours_Studied: With mean

Checked data types and column consistency

🚨 Outlier Handling
Exam_Score: Replaced scores >100 or <0 with the mean score

Attendance: Identified any values outside 0–100 (for review only)

📊 Key Analysis Performed
Total Students: Printed total count

Duplicate Records: Checked and counted

Null Value Summary: Before and after filling

Unique Values: For gender and exam score

Value Counts: For distance from home

🔎 Insights & GroupBy Analysis
Average Exam Score by Hours Studied

Average Attendance by Gender

Average Exam Score by Extracurricular Activities

Average Hours Studied by Parental Education Level

Top 10 Students by Exam Score

List of Students with Exam Score Between 40–60

Average Exam Score: Male vs Female

Most Common Parental Education Level

Correlation between Exam Score and Attendance

🧠 Interesting Patterns Observed
Students with more study hours scored better.

Female vs Male score comparison.

High correlation (or lack thereof) between attendance and score.

Participation in extracurricular activities vs performance.


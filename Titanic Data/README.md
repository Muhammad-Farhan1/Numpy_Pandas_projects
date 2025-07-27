# Titanic Dataset Analysis 🛳️

This project is a beginner-friendly data analysis of the Titanic dataset using Python and Pandas.

## 📁 Dataset
The dataset used is `Titanic-Dataset.csv`, which contains information about passengers aboard the Titanic, including:
- Passenger ID
- Name, Age, Gender
- Class (Pclass)
- Fare
- Embarked location
- Survival status

## ✅ Tasks Performed

1. **Load the dataset** using Pandas and inspect the first few rows.
2. **Handle missing values**:
   - Fill missing Age with the mean.
   - Fill missing Cabin with the most frequent value.
   - Fill missing Embarked values with 'U' (Unknown).
3. **Convert categorical data to numeric**:
   - 'Sex': male → 0, female → 1
   - 'Embarked': S → 10, C → 20, Q → 30, U → 0
4. **Analyze survival data**:
   - Number of male vs female survivors
   - Survival rate by Pclass
   - Average age of survivors vs non-survivors
5. **Basic statistics**:
   - Total number of passengers
   - Overall survival rate
6. **Advanced grouping**:
   - Survival rate by gender and class (Pclass)

## 📊 Tools Used
- Python
- Pandas



## 🙏 Author
This project was built with dedication by Muhammad Farhan, an aspiring Python developer and ML enthusiast.

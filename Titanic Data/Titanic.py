import pandas as pd

# ============================
# 1. Load and View the Dataset
# ============================

# Load Titanic dataset
df = pd.read_csv("Titanic Data/Titanic-Dataset.csv")

# Check for missing values
# print(df.isnull().sum())


# =======================
# 2. Data Cleaning Tasks
# =======================

# Fill missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Cabin'] = df['Cabin'].fillna(df['Cabin'].mode()[0]) 
df['Embarked'] = df['Embarked'].fillna('U')

# Check again for missing values
# print(df.isnull().sum())


# =================================
# 3. Convert Categorical to Numeric
# =================================

# Convert 'Sex' to numeric: male = 0, female = 1
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Convert 'Embarked' to numeric: S = 10, C = 20, Q = 30, U = 0
df['Embarked'] = df['Embarked'].map({"S": 10, "C": 20, "Q": 30, "U": 0})


# ====================================
# 4. How Many Male vs Female Survived
# ====================================

survivors_by_sex = df[df['Survived']== 1]['Sex'].value_counts()
#print(survivors_by_sex)
# Output: 1 = Female survivors, 0 = Male survivors


# ========================================
# 5. What is the Survival Rate by Pclass?
# ========================================

survival_by_pclass = df.groupby('Pclass')['Survived'].mean() * 100
#print(survival_by_pclass)


# ============================================
# 6. Average Age of Survivors vs Non-Survivors
# ============================================

avg_age_by_survival = df.groupby('Survived')['Age'].mean()
#print("Average Age of Survivors (1) vs Non-Survivors (0):\n")
#print(avg_age_by_survival)


# ======================================
# 7. Find the total number of passengers.
# ======================================

total_Passengers = df['PassengerId']
#print(f"Total number of Passengers are: {len(total_Passengers)}")

# =======================================
# 8.  Calculate the overall survival rate.
# =======================================

survived = df[df['Survived'] == 1].shape[0]
total = len(df)
survival_rate = (survived / total) * 100
#print(f"The survival rate of passengers : {survival_rate:.2f}")

# ===============================================================
# 9. Find the survival rate for each gender within each class.
# ===============================================================

survival_by_gender_class = df.groupby(['Sex', 'Pclass'])['Survived'].mean() * 100

print("Survival Rate for Each Gender Within Each Class:")
print(survival_by_gender_class)


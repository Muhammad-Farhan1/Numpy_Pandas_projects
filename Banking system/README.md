# 🏦 Bank Employee Data Cleaning Project

This project focuses on cleaning a messy banking dataset containing employee details like age, experience, salary, department, rating, and city.

## 🧾 Dataset Summary

The original dataset (`messed_data.csv`) had the following issues:
- Missing values in numeric columns (`Age`, `Experience`, `Salary`, `Rating`)
- Infinite values (e.g., due to division errors or corrupt data)

## 🛠 Data Cleaning Steps

1. **Missing Values**
   - `Age` filled with **mean**
   - `Experience` filled with **median**
   - `Salary` filled with **mean**
   - `Rating` filled with **mean**

2. **Infinite Values**
   - Replaced all infinite values (`np.inf`, `-np.inf`) with `NaN`
   - Then filled those `NaN` values with the **mean** of each numeric column

3. **Final Output**
   - All missing and infinite values handled
   - Cleaned dataset saved as: `Cleaned_Data.csv`

## 🧪 Technologies Used

- Python 🐍
- Pandas 📊
- NumPy 🔢

## 📁 Files in this Project

| File Name        | Description                        |
|------------------|------------------------------------|
| `messed_data.csv` | Raw input dataset with issues      |
| `Cleaned_Data.csv` | Final cleaned dataset              |
| `data_cleaning.py` | Python script for cleaning         |
| `README.md`       | Project overview and documentation |

## 📌 How to Run

1. Clone or download this repo
2. Make sure you have Pandas and NumPy installed
3. Run the script:
   ```bash
   python data_cleaning.py

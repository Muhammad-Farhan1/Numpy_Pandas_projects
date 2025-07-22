# COVID-19 Vaccination Data Analysis

This project performs a basic analysis and cleaning of a COVID-19 vaccination dataset using **Pandas**. It includes data type conversion, missing value handling, duplicate checks, and extraction of key insights.

## 📁 Dataset

The dataset used is `vaccinations.csv`, which contains country-wise vaccination statistics over time.

---

## 📌 Key Operations Performed

### ✅ 1. Data Loading
- Reads the dataset using `pandas.read_csv()`

### ✅ 2. Initial Exploration
- Displays basic info such as:
  - First few rows
  - Data types
  - Summary statistics (`mean`, `min`, `max`, `std`, etc.)

### ✅ 3. Data Cleaning
- Converts the `date` column to `datetime` format for accurate time-based analysis.
- Checks for duplicate rows and removes them if found.
- Handles missing values:
  - Uses `mean` or `median` to fill `NaN` values depending on the column's nature.

### ✅ 4. Analysis Tasks
- **Top 10 countries** with the highest number of fully vaccinated people.
- **First vaccination date** for each country (i.e., when `total_vaccinations > 0`).

---

## 🧹 Missing Value Treatment Strategy

| Column                                | Method  |
|---------------------------------------|---------|
| `total_vaccinations`                 | Mean    |
| `people_vaccinated`                 | Median  |
| `people_fully_vaccinated`          | Median  |
| `total_boosters`                   | Mean    |
| `daily_vaccinations_raw`           | Median  |
| `daily_vaccinations`               | Mean    |
| `total_vaccinations_per_hundred`  | Median  |
| `people_vaccinated_per_hundred`   | Median  |
| `people_fully_vaccinated_per_hundred` | Mean |
| `total_boosters_per_hundred`      | Mean    |
| `daily_vaccinations_per_million`  | Mean    |

---

## 📈 Insights

1. The dataset was free of duplicate rows.
2. All missing values were handled with appropriate statistical techniques.
3. The data type of the `date` column was converted for better time-series analysis.
4. Identified the earliest vaccination date for each country.

---

## 📦 Requirements

- Python 
- pandas

```bash
pip install pandas

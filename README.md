# Netflix-Content-Data-Analysis
Conducted an exploratory data analysis on Netflix’s catalog to evaluate trends in content production. Analyzed genre popularity, country contributions, and year-wise content growth. Applied Pandas for data manipulation and NumPy for statistical calculations. Cleaned and transformed real-world data to derive business insights.

# 🎬 Netflix Movies & TV Shows Data Analysis

This project analyzes the Netflix catalog to uncover trends in content production across years, countries, and genres. It demonstrates the use of **Pandas** and **NumPy** for data cleaning, aggregation, and transformation—key skills for data analysts.

---

## 🧠 Objective

- Understand the distribution of Movies vs. TV Shows
- Identify top contributing countries
- Discover the most common genres
- Analyze growth in content over the years
- Calculate average movie duration using NumPy

---

## 📂 Dataset Overview

Sample dataset: `netflix_data.csv`  
| Column         | Description                          |
|----------------|--------------------------------------|
| `show_id`      | Unique identifier                    |
| `type`         | Type of content (Movie / TV Show)    |
| `title`        | Name of the content                  |
| `director`     | Director's name                      |
| `cast`         | Cast members                         |
| `country`      | Production country                   |
| `date_added`   | Date added to Netflix                |
| `release_year` | Year of release                      |
| `rating`       | Content rating                       |
| `duration`     | Duration of content                  |
| `listed_in`    | Genres or categories                 |
| `description`  | Brief summary                        |

---

## 🛠️ Tools Used

- Python 🐍
- Pandas 📊
- NumPy 🔢
- VS Code
- Jupyter Notebook (optional)

---

## 📌 Features

- Drop duplicates and handle missing data
- Parse and format date columns
- Count and compare content types
- Analyze genres with `str.split()` and `stack()`
- Use `groupby()` to examine yearly growth
- Extract numeric durations using regex
- Use NumPy to calculate average values

---

## 📈 Key Insights

- Total number of Movies vs. TV Shows
- Top 5 countries contributing content
- Most popular genres
- Year-wise content trend over the last 10 years
- Average movie duration in minutes

---

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/Kritikamishraa/Netflix-Content-Data-Analysis.git
cd netflix-data-analysis
```

2. Install requirements:
```bash
pip install pandas numpy
```

3. Run the script:
```bash
python analysis.py
```

4. Or open in VS Code:
```bash
VS Code
```

---

## 📁 Folder Structure

```
📦 netflix-data-analysis/
├── netflix_data.csv
├── analysis.py
├── README.md
```

---

## 👤 Author

**Kritika Mishra**  
📧 Email: kritikamishraa12@gmail.com  
🔗 [LinkedIn]https://www.linkedin.com/in/kritika-mishra-578574317/
🐱 [GitHub]https://github.com/Kritikamishraa/Netflix-Content-Data-Analysis

---

## ✅ Project Status

> Completed ✅ | Skills: `Pandas`, `NumPy`, `Data Cleaning`, `Exploratory Data Analysis`


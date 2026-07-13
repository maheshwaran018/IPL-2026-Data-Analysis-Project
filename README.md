# 🏏 IPL 2026 Data Analysis Project

An end-to-end **IPL 2026 Data Analysis Project** that automates data collection, processes raw cricket statistics, and presents interactive visualizations using Power BI. This project demonstrates practical skills in **Python, Selenium, Pandas, Data Analysis, and Business Intelligence**.

---

## 📌 Project Overview

This project collects IPL 2026 statistics from the official IPL website using Selenium, cleans and structures the data with Pandas, and builds an interactive Power BI dashboard to uncover meaningful insights.

The dashboard helps users analyze:

- 🏆 Team Performance
- 🏏 Player Statistics
- 📈 Batting Trends
- 🎯 Strike Rate Analysis
- 💯 Total Runs
- 🔥 Top Performers
- 📊 Interactive Filters and Visualizations

---

## 🚀 Project Workflow

```
Official IPL Website
          │
          ▼
Python + Selenium
(Web Scraping)
          │
          ▼
Raw Data Collection
          │
          ▼
Pandas
(Data Cleaning & Processing)
          │
          ▼
CSV Dataset
          │
          ▼
Power BI Dashboard
(Data Visualization)
```

---

## ⚙️ Technologies Used

| Technology | Purpose |
|------------|---------|
| 🐍 Python | Web Scraping & Automation |
| 🌐 Selenium | Automated Data Extraction |
| 🐼 Pandas | Data Cleaning & Processing |
| 📄 CSV | Data Storage |
| 📊 Power BI | Interactive Dashboard & Visualization |

---

## 📂 Project Structure

```
IPL-2026-Data-Analysis/
│
├── data/
│   └── IPL2026.csv
│
├── scraper/
│   └── ipl_scraper.py
│
├── dashboard/
│   └── IPL_2026_Dashboard.pbix
│
├── screenshots/
│   ├── dashboard.png
│   ├── batting_analysis.png
│   └── team_analysis.png
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📊 Dashboard Features

### 🏏 Team Analysis
- Team Standings
- Total Runs
- Matches Played
- Win Percentage

### 👤 Player Analysis
- Top Run Scorers
- Strike Rate
- Highest Scores
- Batting Average

### 📈 Performance Insights
- Team Comparison
- Player Comparison
- Runs Distribution
- Interactive Filters

---

## 📸 Dashboard Preview

### Main Dashboard

> Add your dashboard screenshot here

```
screenshots/dashboard.png
```

---

## 🔄 Data Pipeline

### Step 1 — Web Scraping

- Selenium automates browser interactions.
- Extracts player and team statistics.
- Collects latest IPL 2026 season data.

### Step 2 — Data Processing

Using Pandas to:

- Remove duplicates
- Handle missing values
- Format columns
- Export clean CSV

### Step 3 — Visualization

Import the processed CSV into Power BI to create:

- KPI Cards
- Team Rankings
- Bar Charts
- Pie Charts
- Interactive Slicers
- Performance Dashboards

---

## 📥 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/IPL-2026-Data-Analysis.git
```

Move into the project

```bash
cd IPL-2026-Data-Analysis
```

Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually

```bash
pip install selenium pandas
```

---

## ▶️ Run the Project

Run the scraper

```bash
python ipl_scraper.py
```

The script will automatically:

- Open the IPL website
- Scrape player statistics
- Clean the data
- Save

```
IPL2026.csv
```

Open the Power BI file

```
IPL_2026_Dashboard.pbix
```

Refresh the dataset to see the latest statistics.

---

## 📈 Sample Insights

- Which team scored the most runs?
- Who has the highest strike rate?
- Top run scorers of IPL 2026
- Team-wise batting performance
- Overall tournament statistics

---

## 📚 Skills Demonstrated

- Python Programming
- Selenium Automation
- Data Collection
- Web Scraping
- Data Cleaning
- Pandas
- Power BI
- Dashboard Design
- Data Visualization
- Data Analytics

---

## 🎯 Future Improvements

- Live API Integration
- Bowling Statistics
- Match Prediction Model
- Win Probability Analysis
- Machine Learning Integration
- Real-time Dashboard Refresh

---

## 👨‍💻 Author

**Maheshwaran**

- 💼 LinkedIn: https://www.linkedin.com/in/maheshwaranai/
- 💻 GitHub: https://github.com/maheshwaran018

---

## ⭐ If you like this project

Give this repository a ⭐ on GitHub and feel free to contribute!
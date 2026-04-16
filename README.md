# Black Friday Sales Analysis

<p align="center"><strong>A reproducible retail analytics project that combines Python, SQL, statistical testing, and Power BI.</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=for-the-badge&logo=scipy&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />
  <a href="#practical-limits"><img src="https://img.shields.io/badge/Status-Completed-2ea44f?style=for-the-badge" alt="Project status completed" /></a>
</p>

---

## Project Overview

This repository contains the end-to-end data analysis pipeline for the Black Friday Sales dataset. It encompasses everything from the raw data ingestion, transformation formatting, exploratory data analysis, to the final reporting outputs.

This project analyzes Black Friday transaction data to understand how customer demographics, location, and tenure relate to purchase behavior. It includes a Python processing pipeline, a MySQL setup script, a notebook for statistical analysis, and a Power BI report with screenshots.

## Project Structure

``text
root/
├── data/
│   ├── raw/              <- original source CSVs (e.g. black_friday_sales_raw.csv)
│   ├── processed/        <- transformed master tables (e.g. black_friday_sales_master.csv)
│   └── external/         <- third-party datasets
├── notebooks/
│   └── eda/              <- Exploratory workflows (01_black_friday_sales_analysis.ipynb)
├── dashboards/
│   └── powerbi/          <- .pbix files (dashboard.pbix)
├── src/
│   ├── ingestion/        <- Extraction logic (pipeline.py)
│   └── transformation/   <- Cleaning logic (data_processing.py)
├── sql/
│   └── ddl/              <- Schema definitions (mysql_schema.sql)
├── reports/
│   └── figures/          <- Rendered charts and figures
├── tests/                <- Pytest unit and logic checks
├── config/               <- Configuration and environment variables
└── requirements.txt      <- Environment dependency list
``

## Key Findings

- Gender is associated with a meaningful difference in average spend.
- Marital status is not a strong driver of spend in this dataset.
- Age group and city category both show statistically significant differences in spending.
- Tenure shows statistical significance, but the practical impact appears weak. 
- The notebook's main customer profile is a male buyer aged 26 to 35, with early-stage residents also standing out in the analysis.

## Dashboard Preview

<p align="center">
  <img src="./reports/figures/powerbi_dashboard_executive.png" width="85%" alt="Executive dashboard" />
</p>

<p align="center">
  <img src="./reports/figures/powerbi_dashboard_marketing.png" width="85%" alt="Marketing dashboard" />
</p>

<p align="center">
  <img src="./reports/figures/tenure_total_purchase.png" width="85%" alt="Tenure versus total purchase chart" />
</p>

## Setup Instructions
1. Clone the repository to your local machine:
   ``bash
   git clone https://github.com/Dipjyoti-Karmakar/black-friday-sales-analysis.git
   cd black-friday-sales-analysis
   ``
2. Create and activate your virtual environment, then install dependencies:
   ``bash
   # Unix/macOS
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ``
3. Copy config/.env.example to config/.env and update your variables.
4. Run the data ingestion and transformation scripts under /src:
   ``bash
   python -m src.ingestion.pipeline
   python -m src.transformation.data_processing
   ``

## Usage
- Raw data lives in data/raw/ while the finalized tables are saved to data/processed/. (Place the raw file at data/raw/black_friday_sales_raw.csv before running the pipeline).
- Run 	ests/test_pipeline.py with pytest to validate your transformations. 
- You can begin exploring data visually through 
otebooks/eda/01_black_friday_sales_analysis.ipynb.
- Dashboards are available in dashboards/powerbi/ (e.g., dashboard.pbix).

## Tech Stack

Python, pandas, NumPy, SciPy, matplotlib, seaborn, MySQL, PyMySQL, SQLAlchemy, Jupyter, Power BI

## Author

**Dipjyoti Karmakar**  
Data Analyst | Analytics and Business Intelligence  
[LinkedIn Profile](https://www.linkedin.com/in/dipjyoti-karmakar-dk/)  
[dipjyotikarmakar97@gmail.com](mailto:dipjyotikarmakar97@gmail.com)

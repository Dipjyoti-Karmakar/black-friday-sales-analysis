<h1 align="center">Black Friday Sales Analysis</h1>

<p align="center">
  <strong>End-to-end data engineering &amp; analytics pipeline — from raw retail transactions to actionable business intelligence.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Engineering-150458?style=for-the-badge&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=for-the-badge&logo=powerbi&logoColor=black" />
  <img src="https://img.shields.io/badge/Status-Completed-2ea44f?style=for-the-badge" />
</p>

---

## Overview

This project analyzes **537K+ Black Friday retail transactions** to uncover customer purchase behavior across demographics, product categories, and geographic segments. The pipeline ingests raw CSV data, performs cleaning and feature engineering in Python, loads the enriched dataset into MySQL, conducts statistical EDA in Jupyter, and delivers a Power BI dashboard for stakeholder consumption.

### Key Outcomes
- Identified the **"Power Consumer" profile**: Male, aged 26–35, City B, 1–2 year resident.
- Proved via **hypothesis testing** (T-Test / ANOVA) that Gender and City significantly drive spending, while Marital Status does not.
- Engineered **4 custom features** — CLV, Category Breadth, City Loyalty Index, Product Popularity Score — enabling customer segmentation beyond raw demographics.
- Delivered a **Power BI dashboard** surfacing revenue breakdowns, top products, and demographic overlays for business stakeholders.

---

## Architecture & Pipeline

### High-Level Architecture

```mermaid
graph LR
    classDef data fill:#E1F5FE,stroke:#0288D1,stroke-width:2px,color:#01579B
    classDef process fill:#FFF3E0,stroke:#F57C00,stroke-width:2px,color:#E65100
    classDef analytical fill:#E8F5E9,stroke:#388E3C,stroke-width:2px,color:#1B5E20
    classDef output fill:#F3E5F5,stroke:#7B1FA2,stroke-width:2px,color:#4A148C

    A[("🗂 Raw Dataset<br/>537K rows · 12 cols")]:::data
    B["⚙️ Data Cleaning<br/>Python · pandas"]:::process
    C[("📦 Processed Dataset<br/>Enriched master table")]:::data
    D["📊 Exploratory Analysis<br/>Jupyter Notebook"]:::analytical
    E["📈 Power BI Dashboard<br/>Interactive BI layer"]:::analytical
    F(("💡 Business Insights<br/>Strategic recommendations")):::output

    A -->|Ingestion & Validation| B
    B -->|Feature Engineering| C
    C -->|Statistical EDA & Hypothesis Testing| D
    C -->|SQL Integration| E
    D --> F
    E --> F
```

### Data Pipeline Flow

```mermaid
flowchart TD
    subgraph "<b>Stage 1 — Ingestion & Transformation</b>"
        direction TB
        R["data/raw/<br/>Original CSV dataset"] --> P["src/data_pipeline.py<br/>Cleaning · Imputation · Feature Engineering"]
        P --> O["data/processed/<br/>Enriched master CSV"]
    end

    subgraph "<b>Stage 2 — Storage</b>"
        direction TB
        O --> SQL["MySQL Database<br/>BLACK_FRIDAY_DB"]
    end

    subgraph "<b>Stage 3 — Analysis & Reporting</b>"
        direction TB
      SQL --> NB["notebooks/black_friday_sales_analysis.ipynb<br/>Statistical EDA · Hypothesis Testing"]
        SQL --> PBI["Power BI Dashboard<br/>Interactive visualizations"]
        NB --> INS["Business Insights & Recommendations"]
        PBI --> INS
    end
```

---

## Dashboard & Visualizations

### Interactive Dashboard Demo

<p align="center">
  <img src="reports/demo.gif" alt="Black Friday Sales Dashboard — interactive walkthrough" width="90%"/>
</p>

### Final Dashboard Snapshot

<p align="center">
  <img src="reports/figures/powerbi_dashboard_executive.png" alt="Black Friday Sales Dashboard — Executive" width="90%"/>
</p>

### Marketing Dashboard (Page 2)

<p align="center">
  <img src="reports/figures/powerbi_dashboard_marketing.png" alt="Black Friday Sales Dashboard — Marketing" width="90%"/>
</p>

> *Place your Power BI screenshots in `reports/figures/powerbi_dashboard_executive.png` (Executive) and `reports/figures/powerbi_dashboard_marketing.png` (Marketing). Add an animated GIF walkthrough in `reports/demo.gif`.*

---

## Project Structure

```text
black-friday-sales-analysis/
│
├── data/
│   ├── raw/                        # Immutable source data (original CSV)
│   └── processed/                  # Cleaned, feature-enriched master dataset
│
├── notebooks/
│   └── black_friday_sales_analysis.ipynb  # Full EDA: profiling, visualization, hypothesis testing
│
├── src/
│   ├── data_pipeline.py            # Automated cleaning & feature engineering script
│   └── mysql_black_friday_setup.sql # MySQL schema, CSV import, validation views
│
├── reports/
│   ├── figures/
│   │   ├── powerbi_dashboard_executive.png # Power BI — Executive dashboard snapshot (Page 1)
│   │   └── powerbi_dashboard_marketing.png # Power BI — Marketing dashboard snapshot (Page 2)
│   └── demo.gif                    # Animated dashboard walkthrough
│
├── Dataset/                        # Original dataset folder (legacy — preserved for Git history)
├── Pipeline/                       # Original pipeline folder (legacy — preserved for Git history)
│
├── README.md
├── requirements.txt                # Pinned Python dependencies
└── .gitignore
```

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/<your-username>/black-friday-sales-analysis.git
cd black-friday-sales-analysis

# 2. Create a virtual environment & install dependencies
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt

# 3. Run the data pipeline (produces data/processed/black_friday_sales_master.csv)
python src/data_pipeline.py

# 4. (Optional) Set up MySQL database
#    Open src/mysql_black_friday_setup.sql in MySQL Workbench
#    and execute — adjust the LOAD DATA path to your local machine.

# 5. Launch the analysis notebook
jupyter notebook notebooks/black_friday_sales_analysis.ipynb
```

---

## Methodology

| Phase | Tools | Description |
|:------|:------|:------------|
| **Ingestion** | Python, pandas | Read 537K-row CSV; validate schema and types |
| **Cleaning** | pandas, NumPy | Impute nulls in `Product_Category_2/3` with 0; coerce `Stay_In_Current_City_Years` (`4+` → `4`) |
| **Feature Engineering** | pandas | Derive CLV, Category Breadth, City Loyalty Index, Product Popularity Score |
| **Database** | MySQL, SQLAlchemy | Load enriched data; create reporting views (Customer, Product, Transaction) |
| **EDA** | matplotlib, seaborn, SciPy | Histograms, boxplots, heatmaps; T-Tests (Gender, Marital Status), ANOVA (Age, City, Tenure) |
| **Dashboarding** | Power BI | Interactive drill-down dashboard connected to MySQL |

---

## Key Business Insights

| Hypothesis | Test | P-Value | Verdict |
|:-----------|:-----|:--------|:--------|
| Men spend more than Women | Welch's T-Test | < 0.05 | ✅ **Significant** — Males spend ~$703 more per transaction |
| Married ≠ Single spending | Welch's T-Test | 0.73 | ❌ Not significant — $4.73 difference is noise |
| Spending varies by Age Group | One-Way ANOVA | < 0.05 | ✅ **Significant** — 26–35 age group dominates revenue |
| Spending varies by City | One-Way ANOVA | < 0.05 | ✅ **Significant** — City B drives highest volume |
| Tenure affects spending | One-Way ANOVA | < 0.05 | ⚠️ Statistically significant but **practically weak** |

### Strategic Recommendations
1. **Acquire 1-year residents aggressively** — they drive the highest transaction volume and total revenue.
2. **Upsell 2-year residents** — they have the highest average order value; target with premium product campaigns.
3. **Investigate the tenure drop-off** — spending declines sharply at 4+ years; deploy re-engagement strategies.
4. **Deprioritize marital-status segmentation** — no measurable impact on purchasing behavior.

---

## Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white" />
  <img src="https://img.shields.io/badge/Matplotlib-11557C?style=flat-square&logo=plotly&logoColor=white" />
  <img src="https://img.shields.io/badge/Seaborn-3776AB?style=flat-square" />
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white" />
  <img src="https://img.shields.io/badge/Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white" />
  <img src="https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black" />
</p>

---

## Contributing

1. Fork the repository.
2. Create a descriptive branch: `feature/<short-description>`.
3. Open a pull request with a clear summary and any data/visual artifacts.

---

## Contact

**Dipjyoti Karmakar** — [LinkedIn](https://www.linkedin.com/in/dipjyoti-karmakar-dk/)

---

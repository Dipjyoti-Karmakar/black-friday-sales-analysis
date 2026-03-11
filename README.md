# Black Friday Sales Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python) ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas) ![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

## Overview

This repository contains a reproducible end-to-end analysis of Black Friday retail transactions. It provides a clean, well-documented pipeline to ingest the raw data, perform exploratory data analysis (EDA), implement cleaning and feature engineering, and produce a canonical master dataset ready for modelling and reporting.

The primary objectives are:
- Clean and consolidate transaction-level data into a single master dataset.
- Provide analyses and visualizations to surface business insights (top customer segments, highest-value products, spending patterns).
- Deliver a reproducible artifact for downstream modelling or dashboarding.

## Clone the repository

```bash
git clone https://github.com/Dipjyoti-Karmakar/black-friday-sales-analysis.git
```

## Quick Start

Prerequisites:
- Python 3.8+ and `pip`, or a comparable Python environment.
- JupyterLab or Jupyter Notebook for the analysis notebook.
## Recommended Next Steps

- Add a `requirements.txt` with pinned package versions for reproducible environments.
- Add CI checks that run lightweight notebook tests or data sanity checks.
- Convert notebook ETL steps into a parameterized Python script for scheduled runs.

Data quality considerations:
- Missing values are handled explicitly in the notebook using principled imputation and exclusion rules.
- Identifiers and categorical fields are coerced to appropriate types before analysis.

## Analysis Pipeline (high level)

1. Ingest raw CSV from `Dataset/`.
2. Validate and clean fields (null handling, type coercion, inconsistent encodings).
3. Feature engineering (e.g., customer-level aggregates such as total spend, purchase counts, recency proxies).
4. Exploratory analysis and visualizations to answer business questions.
5. Export a reproducible `Pipeline/3.1_Black_Friday_Master_Df.csv` for modelling and reporting.

All processing logic is present in `Pipeline/3.0_Black_Friday_Sales_Analysis.ipynb` and can be adapted into scripts for automation.

## How to Reproduce the Master Dataset

Open and execute the notebook cells sequentially. Key reproducibility notes:
- All file reads/writes use relative paths inside the repository.
- Random seeds (where used) are set in the notebook to ensure deterministic results.
- The final master DataFrame is exported with:

```python
df.to_csv('Pipeline/3.1_Black_Friday_Master_Df.csv', index=False)
```

If you plan to automate, extract the notebook cells into a script and parameterize input/output paths.

## Key Business Questions Addressed

- Which customer segments contribute the most revenue during Black Friday?
- What products or product groups are the highest revenue drivers?
- Can we predict purchase amount from available demographic and product features?
- What customer cohorts should marketing prioritize for retention or upsell?

## Deliverables

- Cleaned master dataset: `Pipeline/3.1_Black_Friday_Master_Df.csv`.
- Analysis notebook with EDA, visualizations, and modelling experiments: `Pipeline/3.0_Black_Friday_Sales_Analysis.ipynb`.
- Optional SQL schema and import script: `Pipeline/2_Black_Friday_Database_Setup.sql`.

## Recommended Next Steps

- Add a `requirements.txt` with pinned package versions for reproducible environments.
- Add CI checks that run lightweight notebook tests or data sanity checks.
- Convert notebook ETL steps into a parameterized Python script for scheduled runs.

## Contribution & Governance

Contributions are welcome. Suggested workflow:
1. Fork the repository.
2. Create a descriptive branch: `feature/<short-description>`.
3. Open a pull request with a clear summary and any data/visual artifacts.

## Contact

For questions, collaboration, or commercial inquiries, please contact:

- Dipjyoti Karmakar — https://www.linkedin.com/in/dipjyoti-karmakar-dk/

---

If you would like, I can:
- Create a `requirements.txt` with pinned versions now.
- Add a permissive `LICENSE` (MIT) and a short `CONTRIBUTING.md`.
- Convert the notebook into a runnable Python ETL script and add a small test harness.

Please tell me which of these you'd like me to do next.

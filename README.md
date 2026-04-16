# Black Friday Sales Analysis

## Project Overview
This repository contains the end-to-end data analysis pipeline for the Black Friday Sales dataset. It encompasses everything from the raw data ingestion, transformation formatting, exploratory data analysis, to the final reporting outputs.

## Project Structure

```text
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
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Create and activate your virtual environment, then install dependencies:
   ```bash
   # Unix/macOS
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt

   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Copy config/.env.example to config/.env and update your variables.
4. Run the data ingestion and transformation scripts under /src:
   ```bash
   python -m src.ingestion.pipeline
   python -m src.transformation.data_processing
   ```

## Usage
- Raw data lives in data/raw/ while the finalized tables are saved to data/processed/.
- Run tests/test_pipeline.py with pytest to validate your transformations. 
- You can begin exploring data visually through notebooks/eda/01_black_friday_sales_analysis.ipynb.
- Dashboards are available in dashboards/powerbi/ (e.g., dashboard.pbix).

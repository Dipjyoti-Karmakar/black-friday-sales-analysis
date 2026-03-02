"""
Black Friday Sales — Data Cleaning & Feature Engineering Pipeline
=================================================================
Author : Dipjyoti Karmakar
Purpose: Ingest the raw Black Friday CSV, apply cleaning rules,
         engineer customer- and product-level features, and export
         the enriched master dataset for BI consumption.

Usage
-----
    python src/data_pipeline.py                       # defaults
    python src/data_pipeline.py --input data/raw/black_friday_sales_raw.csv \
                                --output data/processed/black_friday_sales_master.csv
"""

from __future__ import annotations

import argparse
import pathlib
import sys

import numpy as np
import pandas as pd


CANONICAL_COLUMNS: dict[str, str] = {
    "user_id": "USER_ID",
    "product_id": "PRODUCT_ID",
    "gender": "GENDER",
    "age": "AGE",
    "occupation": "OCCUPATION",
    "city_category": "CITY_CATEGORY",
    "stay_in_current_city_years": "STAY_IN_CURRENT_CITY_YEARS",
    "marital_status": "MARITAL_STATUS",
    "product_category_1": "PRODUCT_CATEGORY_1",
    "product_category_2": "PRODUCT_CATEGORY_2",
    "product_category_3": "PRODUCT_CATEGORY_3",
    "purchase": "PURCHASE",
    "transaction_id": "TRANSACTION_ID",
}


# ───────────────────────────── helpers ─────────────────────────────

def load_raw(path: pathlib.Path) -> pd.DataFrame:
    """Read the raw CSV and return an unmodified DataFrame."""
    df = pd.read_csv(path)

    # Normalize column names so the pipeline works with either Kaggle-style
    # headers (e.g., "User_ID") or uppercase SQL exports (e.g., "USER_ID").
    rename_map: dict[str, str] = {}
    for col in df.columns:
        key = col.strip().lower().replace(" ", "_").replace("-", "_")
        canonical = CANONICAL_COLUMNS.get(key)
        if canonical and canonical != col:
            rename_map[col] = canonical
    if rename_map:
        df = df.rename(columns=rename_map)

    print(f"[LOAD]  {len(df):,} rows × {df.shape[1]} cols from {path.name}")
    return df


def clean(df: pd.DataFrame) -> pd.DataFrame:
    """Apply cleaning / imputation rules identical to the notebook."""
    # Missing product categories → 0 ("No Category")
    for col in ("PRODUCT_CATEGORY_2", "PRODUCT_CATEGORY_3"):
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)

    # Stay_In_Current_City_Years: '4+' → 4, then cast to int
    col_stay = "STAY_IN_CURRENT_CITY_YEARS"
    if col_stay in df.columns:
        df[col_stay] = df[col_stay].replace("4+", "4").astype(int)

    print("[CLEAN] Missing values imputed · dtypes coerced")
    return df


def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """Derive customer-level and product-level features."""

    # ── Customer-level aggregates ──────────────────────────────────
    customer = df.groupby("USER_ID").agg(
        TOTAL_SPENT=("PURCHASE", "sum"),
        TRANSACTION_COUNT=("PURCHASE", "count"),
        AVG_SPENT=("PURCHASE", "mean"),
        CATEGORY_BREADTH=("PRODUCT_CATEGORY_1", "nunique"),
        STAY_YEARS=("STAY_IN_CURRENT_CITY_YEARS", "max"),
    )
    customer["CLV"] = customer["TOTAL_SPENT"] / customer["TRANSACTION_COUNT"]
    customer["CITY_LOYALTY_INDEX"] = customer["AVG_SPENT"] * customer["STAY_YEARS"]

    # ── Product-level popularity ───────────────────────────────────
    product_pop = (
        df.groupby("PRODUCT_ID")["PURCHASE"]
        .count()
        .reset_index()
        .rename(columns={"PURCHASE": "PRODUCT_POPULARITY_SCORE"})
    )

    # ── Merge back ─────────────────────────────────────────────────
    master = df.merge(product_pop, on="PRODUCT_ID", how="left")
    master = master.merge(
        customer.drop(columns=["STAY_YEARS"]).reset_index(),
        on="USER_ID",
        how="left",
    )

    print(f"[FEAT]  +{len(customer.columns)} customer features · +1 product feature")
    return master


def save(df: pd.DataFrame, path: pathlib.Path) -> None:
    """Write the master DataFrame to CSV."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
    print(f"[SAVE]  {len(df):,} rows → {path}")


# ───────────────────────────── main ────────────────────────────────

def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Black Friday data pipeline")
    parser.add_argument(
        "--input",
        type=pathlib.Path,
        default=pathlib.Path("data/raw/black_friday_sales_raw.csv"),
        help="Path to the raw CSV file",
    )
    parser.add_argument(
        "--output",
        type=pathlib.Path,
        default=pathlib.Path("data/processed/black_friday_sales_master.csv"),
        help="Destination for the enriched master CSV",
    )
    args = parser.parse_args(argv)

    df = load_raw(args.input)
    df = clean(df)
    df = engineer_features(df)
    save(df, args.output)
    print("[DONE]  Pipeline finished successfully ✓")


if __name__ == "__main__":
    main()

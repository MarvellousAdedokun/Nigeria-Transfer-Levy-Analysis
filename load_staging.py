import argparse
import csv
import os
import sys
from collections import defaultdict
from pathlib import Path

import mysql.connector
from dotenv import load_dotenv

load_dotenv()

STAGING_CSV = Path("data/interim/staging_table1.csv")

STAGING_COLUMNS = ["source_file", "source_path", "source_container", "sha256", "archive_sha256", "sheet", "title_cell", "title_raw", "revenue_period_raw", "allocation_period_raw", "allocation_period_source", "header_row", "header_cell", "header_label_raw", "row_label_cell", "row_label_raw", "cell", "value_raw", "row_type", "emtl_found", "status", "total_label_cell", "emtl_total_cell", "emtl_total_value_raw", "overall_total_cell", "overall_total_value_raw", "detail_sum_raw", "sum_matches_total", "warning",]

MAPPING_COLUMNS = ["row_label_raw", "recipient_category", "review_status"]

def read_csv(path: Path, columns: list[str]) -> list[tuple]:
    """Read a CSV (UTF-8, BOM tolerated) and return tuples in column order; empty strings become NULL."""
    with path.open(newline="", encoding="utf-8-sig") as fh:
        reader = csv.DictReader(fh)
        missing = [c for c in columns if c not in (reader.fieldnames or [])]
        if missing:
            raise ValueError(f"Missing columns in {path}: {missing}")
        return [tuple(row[c] if row[c] != "" else None for c in columns) for row in reader]

# Temporary test loop for Block 1
if __name__ == "__main__":
    print("Testing file reader...")
    rows = read_csv(STAGING_CSV, STAGING_COLUMNS)
    print(f"Success! Read {len(rows)} clean rows from CSV.")

import mysql.connector

print("Attempting database connection...")
conn = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT", 3306)),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    database=os.getenv("MYSQL_DATABASE")
)
print("Database connection handshake successful!")
conn.close()
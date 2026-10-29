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

def connect():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        port=int(os.environ.get("MYSQL_PORT", "3306")),
        user=os.environ["MYSQL_USER"],
        password=os.environ["MYSQL_PASSWORD"],
        database=os.environ.get("MYSQL_DATABASE", "emtl_analysis"),
    )

def load_staging(conn) -> int:
    rows = read_csv(STAGING_CSV, STAGING_COLUMNS)
    by_path = defaultdict(list)
    path_idx = STAGING_COLUMNS.index("source_path")
    for row in rows:
        by_path[row[path_idx]].append(row)
    insert = (f"INSERT INTO stg_emtl_table1 ({', '.join(STAGING_COLUMNS)}) "
              f"VALUES ({', '.join(['%s'] * len(STAGING_COLUMNS))})")
    cur = conn.cursor()
    for source_path, group in by_path.items():
        cur.execute("DELETE FROM stg_emtl_table1 WHERE source_path = %s", (source_path,))
        cur.executemany(insert, group)
        print(f"{source_path}: {len(group)} rows")
    print(f"Staging: {len(rows)} rows from {len(by_path)} workbooks.")
    return len(rows)

def load_mapping(conn) -> int:
    rows = read_csv(MAPPING_CSV, MAPPING_COLUMNS)
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO recipient_mapping (row_label_raw, recipient_category, review_status) "
        "VALUES (%s, %s, %s) "
        "ON DUPLICATE KEY UPDATE recipient_category = VALUES(recipient_category), "
        "review_status = VALUES(review_status)",
        rows,
    )
    print(f"Mapping: {len(rows)} labels.")
    return len(rows)
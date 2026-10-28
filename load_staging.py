import os
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

csv_path = "data/interim/staging_table1.csv"
print(f"Checking for file at: {csv_path}")

df = pd.read_csv(csv_path, encoding='utf-8-sig')
print("file read successfully")
print(f"Rows found: {len(df)}")
print(f"Columns found: {len(df.columns)}")

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
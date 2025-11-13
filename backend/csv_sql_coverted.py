import pandas as pd
import sqlite3
import os
import re

CSV_FILE = 'amazon_reviews_master.csv'
DB_FILE = 'amazon_reviews.db'
TABLE_NAME = 'reviews'

def clean_col_name(col_name):
    """Cleans column names for SQL compatibility."""
    col_name = col_name.replace('.', '_')
    col_name = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', col_name)
    return col_name.lower()

if os.path.exists(DB_FILE):
    os.remove(DB_FILE)
    print(f"Removed old database '{DB_FILE}'")

print(f"Loading '{CSV_FILE}'...")
df = pd.read_csv(CSV_FILE, low_memory=False)

df.columns = [clean_col_name(col) for col in df.columns]
print("Cleaned column names for SQL.")

print(f"Writing {len(df)} rows to '{DB_FILE}'...")
conn = sqlite3.connect(DB_FILE)
df.to_sql(TABLE_NAME, conn, if_exists='replace', index=False)
conn.close()

print("Database created successfully!")
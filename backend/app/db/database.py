# backend/app/db/database.py

import sqlite3
from pathlib import Path

from app.db.paths import DATA_DIR, DB_PATH
from app.db.schema_sql import SCHEMA_SQL


def get_connection() -> sqlite3.Connection:
    """
    Open a connection to the SQLite database file.

    SQLite is file-based: connecting to DB_PATH will create the file if it doesn't exist.
    """
    # Ensure the data directory exists (backend/.data/)
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    # Return rows like dictionaries (so row["id"] works instead of row[0])
    conn.row_factory = sqlite3.Row

    # IMPORTANT: SQLite does not enforce foreign keys unless we turn them on per connection.
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db() -> None:
    """
    Create all tables (safe to run multiple times).

    We use CREATE TABLE IF NOT EXISTS in the schema so reruns don't break.
    """
    conn = get_connection()
    try:
        cur = conn.cursor()
        for statement in SCHEMA_SQL:
            cur.execute(statement)
        conn.commit()
    finally:
        conn.close()

import sqlite3

DB_PATH = "database/database.db"


def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)

    cursor.execute("""
    INSERT INTO predictions
    (username, hemoglobin, rbc, platelets, mcv, mch, mchc, pdw, result)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        session["user"],
        hemoglobin,
        rbc,
        platelets,
        mcv,
        mch,
        mchc,
        pdw,
        disease[0]
    ))
    conn.commit()
    conn.close()
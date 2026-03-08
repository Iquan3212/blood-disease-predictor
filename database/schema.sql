CREATE TABLE IF NOT EXISTS predictions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    hemoglobin REAL,
    rbc REAL,
    platelets REAL,
    mcv REAL,
    mch REAL,
    mchc REAL,
    pdw REAL,
    result TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
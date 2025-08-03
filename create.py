import sqlite3

conn = sqlite3.connect("sensor_data.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS sensor_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    temperature REAL,
    humidity REAL,
    potentiometer INTEGER
)
''')

conn.commit()
conn.close()

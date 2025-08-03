import sqlite3
import csv

conn = sqlite3.connect("sensor_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM sensor_log")
rows = cursor.fetchall()

with open("sensor_log.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([desc[0] for desc in cursor.description])  # headers
    writer.writerows(rows)

conn.close()

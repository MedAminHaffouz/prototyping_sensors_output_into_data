import serial
import sqlite3
from datetime import datetime

# Update this to match your Arduino serial port
SERIAL_PORT = '/dev/ttyUSB0'  # Linux
# SERIAL_PORT = 'COM3'        # Windows
BAUD_RATE = 9600

# Connect to serial
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

# Connect to SQLite DB
conn = sqlite3.connect("sensor_data.db")
cursor = conn.cursor()

print(f"[✔] Listening on {SERIAL_PORT}")

try:
    while True:
        line = ser.readline().decode('utf-8').strip()
        if not line or 'NaN' in line:
            continue

        try:
            temp_str, hum_str, pot_str = line.split(',')
            temperature = float(temp_str)
            humidity = float(hum_str)
            potentiometer = int(pot_str)
            timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')

            cursor.execute('''
                INSERT INTO sensor_log (timestamp, temperature, humidity, potentiometer)
                VALUES (?, ?, ?, ?)
            ''', (timestamp, temperature, humidity, potentiometer))
            conn.commit()

            print(f"[{timestamp}] 🌡 {temperature}°C | 💧 {humidity}% | 🎚 {potentiometer}")

        except ValueError:
            print("[!] Failed to parse line:", line)

except KeyboardInterrupt:
    print("\n[!] Stopped by user")

finally:
    conn.close()
    ser.close()

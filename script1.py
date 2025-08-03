import serial
from datetime import datetime

# Replace with your actual port:
# - Windows: 'COM3' or 'COM5'
# - Linux: '/dev/ttyUSB0' or '/dev/ttyACM0'
SERIAL_PORT = '/dev/ttyUSB0'  # <-- Change this
BAUD_RATE = 9600

# Open serial connection
ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
print("Listening on", SERIAL_PORT)

while True:
    try:
        line = ser.readline().decode('utf-8').strip()
        if not line:
            continue

        parts = line.split(',')

        # Skip malformed lines
        if len(parts) != 3 or 'NaN' in line:
            print("[!] Invalid reading:", line)
            continue

        # Extract values
        temp = float(parts[0])
        humidity = float(parts[1])
        pot = int(parts[2])

        # Add system time
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Pretty print
        print(f"[{timestamp}] 🌡 Temp: {temp}°C | 💧 Humidity: {humidity}% | 🎚 Pot: {pot}")

    except KeyboardInterrupt:
        print("\n[!] Exiting listener...")
        break

    except Exception as e:
        print("[!] Error:", e)

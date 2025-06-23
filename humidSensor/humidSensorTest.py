import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Adafruit_DHT
import mysql.connector
import time

from secure_config import db_config

sensor = Adafruit_DHT.DHT11
pin = 4
print("[BOOT] humidSensor 시작됨",flush=True)
try:
    conn = mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"],
        database=db_config["database"]
    )

    

except Exception as e:
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{now}/Error] {e}")

cursor= conn.cursor()    

while True:
    humidity, temperature = Adafruit_DHT.read(sensor, pin)
    if humidity is not None and temperature is not None:
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] : Temp={temperature:.1f}C, Humidity={humidity:.1f}%",flush=True)
        
        cursor.execute(
            "INSERT INTO environment_log (envrm_temp, envrm_humid) VALUES (%s, %s)",
            (temperature, humidity)
        )
        conn.commit()
        time.sleep(1800)
    else:
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] 센서 읽기 실패",flush=True)
        time.sleep(5)

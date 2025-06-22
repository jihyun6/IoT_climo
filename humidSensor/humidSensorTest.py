import Adafruit_DHT
import mysql.connector
import time

sensor = Adafruit_DHT.DHT11
pin = 4
print("[BOOT] humidSensor 시작됨",flush=True)
try:
    conn = mysql.connector.connect(
        host="192.168.45.171",
        user="root",
        password ="1587",
        database="IOT01"
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
            "INSERT INTO temp_humid_log (temperature, humidity) VALUES (%s, %s)",
            (temperature, humidity)
        )
        conn.commit()
        time.sleep(1800)
    else:
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"[{now}] 센서 읽기 실패",flush=True)
        time.sleep(5)

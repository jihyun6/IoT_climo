import RPi.GPIO as GPIO
import time
import os

PIR_PIN = 17  # PIR 센서가 연결된 GPIO 핀 번호

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print(" PIR 센서 감지 대기 중...")

try:
    detected_time = None
    while True:
        if GPIO.input(PIR_PIN) == GPIO.HIGH:
            if detected_time is None:
                detected_time = time.time()
                print(" 사람 감지 시작")

            elif time.time() - detected_time >= 5:
                print(" 5초 이상 감지됨! 사진 촬영합니다.")
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"/home/pi/Desktop/capture_{timestamp}.jpg"
                
                os.system(f"libcamera-still -t 2000 --preview --autofocus-on-capture -o {filename}")
                print(f"✅ 사진 저장 완료: {filename}")
                detected_time = None  # 다음 감지를 위해 초기화
                time.sleep(5)  # 중복 방지를 위해 5초 대기

        else:
            if detected_time is not None:
                print("🙅 감지 취소 (사람 사라짐)")
            detected_time = None

        time.sleep(0.2)

except KeyboardInterrupt:
    print("\n프로그램 종료")

finally:
    GPIO.cleanup()
import RPi.GPIO as GPIO
import cv2
import time
from datetime import datetime

# GPIO 설정
PIR_PIN = 17
#보드에 적힌거랑 같은 번호로 연결
#BCM은 Broadcom 칩 기준 번호 체계로 GPIO 17이면 실제 보드의 핀 번호 11에 해당
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)


print(" PIR 센서 초기화 중 (15초 대기)")
time.sleep(15)  # 초기화 시간

print("PIR 센서 모니터링 시작")



pirState = False  # 처음엔 감지 없음

try:
    while True:
        val = GPIO.input(PIR_PIN)

        if val==1 and not pirState:
            print(" 사람 감지됨!")
            pirState = True
        elif val==0 and pirState:
            print("감지 없음")
            pirState = False

        time.sleep(1)  # 너무 빠른 감지는 필터링
        pirState = False
        
        print("현재 PIR 상태:", GPIO.input(PIR_PIN))
except KeyboardInterrupt:
    print("종료합니다.")

finally:
    print("start cleanup")
    GPIO.cleanup()

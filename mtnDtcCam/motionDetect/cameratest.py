import serial
import time
import os

# 1. 시리얼 포트 열기
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=2)
time.sleep(2)

# 2. 캡처 명령어 (PTC06 명령 프로토콜을 따름)
# 아래 명령어는 예시로, 실제 명령어는 데이터시트 참고
TAKE_PICTURE_CMD = bytes([0x56, 0x00, 0x36, 0x01, 0x00])

# 3. 명령 전송
ser.write(TAKE_PICTURE_CMD)

# 4. 응답 수신 및 이미지 데이터 받기
# (여기엔 데이터 길이 계산, JPEG 헤더 찾기 등 추가 코드 필요)

# 5. 예를 들어 수신된 JPEG 바이트 저장
jpeg_data = b""
while True:
    chunk = ser.read(1024)
    if not chunk:
        break
    jpeg_data += chunk
    if jpeg_data.endswith(b'\xff\xd9'):  # JPEG 종료 마커
        break
    
save_path = os.path.abspath("captured.jpg")
with open(save_path, "wb") as f:
    f.write(jpeg_data)

print(f"📸 이미지 저장 완료: {save_path}")

ser.close()

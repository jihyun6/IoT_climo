import serial
import time

# 시리얼 포트 설정
ser = serial.Serial('/dev/ttyUSB0', 38400, timeout=2)

# 초기화 전, 시리얼 버퍼 비우기
ser.reset_input_buffer()
ser.reset_output_buffer()
time.sleep(1)


# 헬퍼 함수: 명령어 전송 후 응답 받기
def send_cmd(cmd, delay=0.1, resp_len=5):
    ser.write(cmd)
    time.sleep(delay)
    return ser.read(resp_len)

# 카메라 초기화 (reset)
def reset_camera():
    print("Resetting camera...")
    cmd = b'\x56\x00\x26\x00'
    resp = send_cmd(cmd, delay=2)
    print("Reset response:", resp)

# 사진 촬영
def take_picture():
    print("Taking picture...")
    cmd = b'\x56\x00\x36\x01\x00'
    resp = send_cmd(cmd)
    print("Capture response:", resp)

# 이미지 크기 가져오기
def get_image_length():
    cmd = b'\x56\x00\x34\x01\x00'
    ser.write(cmd)
    time.sleep(0.1)
    resp = ser.read(9)
    if resp[0:5] != b'\x76\x00\x34\x00\x04':
        print("Unexpected length response:", resp)
        return None
    length = resp[7] * 256 + resp[8]
    print("Image size:", length, "bytes")
  #  return length

# 이미지 데이터 요청 및 저장
def read_image(length):
    print("Reading image data...")
    # Read command: 0x56 0x00 0x32 0x0C 0x00 0x0A addrH addrM addrL sizeH sizeM sizeL delayH delayL
    addr = [0x00, 0x00, 0x00]
    sizeH = (length >> 8) & 0xFF
    sizeL = length & 0xFF
    cmd = bytes([0x56, 0x00, 0x32, 0x0C, 0x00, 0x0A,
                 addr[0], addr[1], addr[2],
                 0x00, sizeH, sizeL,
                 0x00, 0x0A])
    ser.write(cmd)
    time.sleep(0.5)
    data = ser.read(length + 5)
    # 응답 앞부분 제거하고 저장
    if data[0:5] != b'\x76\x00\x32\x00\x00':
        print("Unexpected image response header:", data[:5])
        return
    image_data = data[5:]
    with open("ptc06_capture.jpg", "wb") as f:
        f.write(image_data)
    print("Saved as ptc06_capture.jpg")

# 전체 흐름
reset_camera()
take_picture()
length = get_image_length()
if length:
    read_image(length)

ser.close()

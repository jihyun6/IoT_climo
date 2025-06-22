import cv2
import RPi.GPIO as GPIO
import time

# PIR 핀 번호 설정
PIR_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

# 얼굴 인식용 Haar Cascade 로드
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 카메라 초기화
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ 카메라 열기 실패")
    exit()

print("📡 PIR 센서 감지 대기 중...")

try:
    detected_time = None
    capturing = False

    while True:
        pir_state = GPIO.input(PIR_PIN)
        ret, frame = cap.read()
        if not ret:
            print("❌ 프레임 읽기 실패")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # PIR 감지 시작
        if pir_state == GPIO.HIGH:
            if detected_time is None:
                detected_time = time.time()
                print("👤 사람 감지 시작")
            elif time.time() - detected_time >= 5 and not capturing:
                print("📸 5초 이상 감지됨. 얼굴 인식 중... (모니터로 확인 가능)")
                capturing = True  # 중복 캡처 방지

        else:
            detected_time = None
            capturing = False

        # 얼굴 감지되면 사진 저장
        if capturing and len(faces) > 0:
            print("✅ 얼굴 감지됨! 사진 저장")
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"/home/pi/Desktop/face_{timestamp}.jpg"
            cv2.imwrite(filename, frame)
            print(f"📂 저장 위치: {filename}")
            capturing = False  # 한번만 찍고 대기

        # 실시간 영상 출력
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow("👁 실시간 얼굴 감지", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("🛑 종료합니다.")
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
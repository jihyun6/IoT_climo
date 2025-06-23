import cv2
import time

def dont_run_camera2():
    duration=15
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    time.sleep(2)

    start_time = time.time()

    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            print("카메라를 열 수 없습니다.")
            break

        cv2.imshow("USB Camera", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


def run_camera():
    duration = 15
    face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/climo/mtnDtcCam/haarcascade_frontalface_default.xml')
    print("로드 성공 여부:", face_cascade.empty())  # False면 정상, True면 실패

    cap = cv2.VideoCapture(1)  # USB 카메라 번호 확인 (0 또는 1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    time.sleep(2)
    start_time = time.time()
    captured = False  # 한 번만 캡처하도록 플래그

    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if not ret:
            print("카메라를 열 수 없습니다.")
            break

        # 창 없이 CLI에서 실행할 경우 주석처리하거나 제거
        cv2.imshow("USB Camera", frame)
        if cv2.waitKey(1) == 27:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        if len(faces) > 0:
            if not captured:
                timestamp = time.strftime("%Y%m%d_%H%M%S")
                filename = f"/home/pi/Desktop/climo/mtnDtcCam/capture_logs/capture_{timestamp}.jpg"
                cv2.imwrite(filename, frame)
                print(f"✅ 정면 감지됨! 사진 저장 완료: {filename}")
                captured = True
                break
        else:
            print("얼굴이 인식되도록 정면을 봐주세요.")

        

        time.sleep(0.5)  # CPU 부담 방지

    cap.release()
    cv2.destroyAllWindows()
import cv2

cap = cv2.VideoCapture(1)  # ← video1이 USB 스트림임

# MJPEG 포맷이 지원된다면 아래 설정도 시도 가능
# cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while True:
    ret, frame = cap.read()
    if not ret:
        print("카메라를 열 수 없습니다.")
        break

    print("frame size:", frame.shape)

    cv2.imshow("USB Camera", frame)
    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()
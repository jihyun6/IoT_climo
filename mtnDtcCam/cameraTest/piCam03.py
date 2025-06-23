import cv2

cap = cv2.VideoCapture(0)

# 해상도 명시
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

ret, frame = cap.read()
if ret:
    print("프레임 크기:", frame.shape)
    cv2.imwrite("test.jpg", frame)
else:
    print("프레임 읽기 실패")

cap.release()
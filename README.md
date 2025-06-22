
## 1️⃣ 주제선정 배경   
 Climo는 실내 환경 모니터링과 보안 감지 기능을 통합한 IoT 기반 스마트 감시 시스템입니다. PIR 센서, 온습도 센서(DHT), 카메라 모듈을 연동하고, Flask API와 React 대시보드를 통해 실시간 상태를 시각화합니다. 스마트홈 수요 증가와 함께 효율적인 에너지 관리, 개인 맞춤형 알림, 비접촉 감시 시스템에 대한 수요가 커지고 있습니다. 특히 1인 가구, 고령자 가구, 무인 매장 등에서는 자동화된 환경 인식 및 침입 탐지 기능이 실용적인 가치를 가집니다.

 본 프로젝트는 이러한 사회적 흐름에 맞춰 "움직임 기반의 반응형 데이터 수집"과 "사용자 맞춤 알림"을 통해 더 똑똑한 공간을 구현하고자 기획되었습니다. 



## 2️⃣ 개발 환경   
|분류   |개발 환경|
|:---:|---|
| 운영체제   |Windows 11, Raspberry Pi4|
| 개발도구   |Python3, ERDCloud, Vs code, phpmysql|
| 개발언어   |Python, JavaScript, React|
| 형상 관리   |Git|
| WAS   |Apache2|
| DB & ORM   |MySql|
| 프레임워크 |Flask|
| 오픈 소스   |Open Wheather, Web Socket, ChartJS, Apache POI|
| Sensor  | DHT11, Pir Sensor, QSenn usb camera|  
 


## 3️⃣  주요기능   
DHT11 센서를 이용하여 온습도 수집  
SONY IMX219(카메라)를 이용하여 사진 캡쳐  
사진 데이터 분석 후 얼굴 인식 기반 개인 맞춤 안내  
모션 트리거 기반 환경 기록  

# 🤖 카미봇파이 (KamibotPi) 파이썬 메소드 레퍼런스

> 카미봇파이를 파이썬으로 제어하기 위한 패키지별 메소드 정리  
> 환경: Python 3.11 · miniConda · VS Code · HelloAI 3.4

---

## 📦 패키지 개요

### 1. `pyKamipi` — 카미봇 하드웨어 제어 패키지

카미봇파이 로봇의 모터, LED, 버저 등 물리적 하드웨어를 직접 제어하기 위한 패키지.  
USB 동글(FTDI CDC 드라이버)을 통해 시리얼 통신(COM 포트, 57600bps)으로 로봇과 연결된다.

```python
from pyKamipi.pibot import *
```

---

### 2. `helloai` — AI 교육용 라이브러리

Arduino의 `setup()` / `loop()` 구조와 동일한 방식으로 카메라 영상 처리, 티처블머신 모델 연동, 윈도우 출력을 쉽게 구현할 수 있는 AI 교육 전용 Python 라이브러리.  
Teachable Machine에서 학습한 `keras_model.h5` 모델을 불러와 실시간 이미지 분류에 사용한다.

```python
from helloai import *
```

---

### 3. `keyboard` — 키보드 입력 감지 패키지

파이썬 프로그램 실행 중 키보드 입력을 실시간으로 감지하는 범용 패키지.  
카미봇 자율주행 중 긴급 정지(`ESC`) 등 인터럽트 처리에 주로 사용된다.

```python
import keyboard
```

---

## 🔧 패키지별 메소드 정리

---

### 📌 `pyKamipi.pibot` — KamibotPi 클래스

#### 객체 생성 및 연결

| 메소드 | 설명 |
|--------|------|
| `KamibotPi(port, baudrate)` | 카미봇 객체 생성 및 연결. `port`: COM 포트 번호 (예: `'COM3'`), `baudrate`: 통신 속도 (기본값 `57600`) |
| `kamibot.close()` | 카미봇 연결 해제 |

```python
kamibot = KamibotPi('COM3', 57600)
kamibot.close()
```

> ⚠️ COM 포트 번호는 PC마다 다름. 장치관리자 → 포트(COM & LPT) → `USB Serial Port(COMx)` 에서 확인

---

#### 💡 LED 제어

| 메소드 | 설명 |
|--------|------|
| `turn_led(r, g, b)` | LED 색상 설정. R·G·B 각각 `0~255` 범위 |

```python
kamibot.turn_led(255, 0, 0)    # 빨간색
kamibot.turn_led(0, 0, 255)    # 파란색
kamibot.turn_led(0, 0, 0)      # 끄기
```

---

#### 🎵 소리 제어

| 메소드 | 설명 |
|--------|------|
| `melody(음계, 시간)` | 버저로 멜로디 재생. 음계(도·레·미 등)와 지속 시간(초) 지정 |
| `kamibot.delay(seconds)` | 지정한 시간(초) 동안 대기 |

```python
kamibot.delay(0.5)    # 0.5초 대기
```

---

#### 🚗 이동 제어

| 메소드 | 파라미터 | 설명 |
|--------|----------|------|
| `stop()` | — | 모터 정지 |
| `go_forward_speed(left, right)` | `0~255` | 앞으로 전진. 좌우 모터 속도를 개별 지정 (속도 차이로 방향 조절) |
| `go_dir_speed(ldir, lspeed, rdir, rspeed)` | `ldir/rdir`: `'f'`(앞) 또는 `'b'`(뒤), `lspeed/rspeed`: `0~255` | 좌우 모터 방향과 속도를 각각 지정하여 이동 |
| `move_forward_unit(value, opt, speed)` | `value`: 이동값, `opt`: 단위 옵션, `speed`: `0~255` | 단위를 지정하여 앞으로 이동 |
| `move_backward_unit(value, opt, speed)` | `value`: 이동값, `opt`: 단위 옵션, `speed`: `0~255` | 단위를 지정하여 뒤로 이동 |

**`opt` 단위 옵션:**

| 값 | 단위 |
|----|------|
| `"-l"` | cm (센티미터) |
| `"-t"` | 초 (시간 기반) |
| `"-s"` | step 단위 (`1 step = 0.0471 cm`) |

```python
kamibot.stop()
kamibot.go_forward_speed(30, 30)              # 직진 (속도 30)
kamibot.go_forward_speed(20, 60)              # 왼쪽으로 커브
kamibot.go_forward_speed(60, 20)              # 오른쪽으로 커브
kamibot.go_dir_speed('f', 100, 'b', 100)      # 제자리 회전
kamibot.move_forward_unit(5, "-l", 100)       # 5cm 앞으로, 속도 100
kamibot.move_backward_unit(5, "-l", 100)      # 5cm 뒤로, 속도 100
```

---

#### 🔄 회전 제어

| 메소드 | 파라미터 | 설명 |
|--------|----------|------|
| `turn_right_speed(value, speed)` | `value`: 회전각 `0~360`, `speed`: `0~255` | 제자리에서 오른쪽으로 각도 회전 |
| `turn_left_speed(value, speed)` | `value`: 회전각 `0~360`, `speed`: `0~255` | 제자리에서 왼쪽으로 각도 회전 |

```python
kamibot.turn_right_speed(90, 150)    # 오른쪽으로 90도 회전
kamibot.turn_left_speed(90, 150)     # 왼쪽으로 90도 회전
kamibot.turn_right_speed(144, 150)   # 오른쪽으로 144도 회전 (오각형 그리기)
```

---

### 📌 `helloai` — AI 라이브러리

#### 윈도우 출력

| 메소드 | 설명 |
|--------|------|
| `Window(name)` | 영상 출력 창 생성. `name`: 창 이름 문자열 |
| `wnd.show(img)` | 카메라 이미지를 창에 표시 |

```python
wnd = Window('main')
wnd.show(img)
```

---

#### 카메라

| 메소드 | 파라미터 | 설명 |
|--------|----------|------|
| `Camera(num, crop, flip)` | `num`: 카메라 번호 (무선 카메라: `0`), `crop`: 정사각형 크롭 여부 (`True`면 480×480), `flip`: 좌우 반전 (`1`이면 반전) | 카메라 객체 생성 |
| `camera.read()` | — | 현재 카메라 프레임 읽기 → `img` 객체 반환 |
| `img.resize(w, h)` | 가로×세로 픽셀 | 이미지 크기 변환 (티처블머신 입력 크기 `224×224` 맞추기용) |

```python
camera = Camera(num=0, crop=True, flip=1)

def loop():
    img = camera.read()
    img = img.resize(224, 224)    # 티처블머신 입력 크기로 변환
    wnd.show(img)
```

---

#### 티처블머신 AI 모델

| 메소드 | 설명 |
|--------|------|
| `TMImageModel()` | 티처블머신 이미지 분류 모델 객체 생성 |
| `model.load_model(path)` | 지정 경로에서 `keras_model.h5` + `labels.txt` 로드. 경로는 영문·공백 없이 지정 |
| `model.process(img)` | 이미지를 모델에 입력하여 분류 결과 레이블 문자열 반환 |

```python
model = TMImageModel()

def setup():
    model.load_model('C:/model/auto')    # keras_model.h5 + labels.txt 위치

def loop():
    img = camera.read()
    img = img.resize(224, 224)
    lbl = model.process(img)
    print(lbl)
```

> 📂 모델 파일 경로 규칙: C 드라이브 내 폴더 생성, **한글·띄어쓰기 사용 금지**  
> 예: `C:/model/auto/keras_model.h5`, `C:/model/auto/labels.txt`

---

#### 실행 구조

`helloai`는 Arduino 방식과 동일한 `setup()` / `loop()` 구조를 사용한다.

| 함수 | 설명 |
|------|------|
| `def setup()` | 프로그램 시작 시 한 번만 실행 (모델 로드, 초기화 등) |
| `def loop()` | 반복 실행되는 메인 루프 (카메라 읽기, 분류, 로봇 제어 등) |
| `run()` | `setup()` 호출 후 `loop()` 를 지속 반복 실행 |

```python
if __name__ == '__main__':
    run()
```

---

### 📌 `keyboard` — 키보드 입력

| 메소드 | 설명 |
|--------|------|
| `keyboard.read_key()` | 키가 눌릴 때까지 대기 후 눌린 키 값 반환 |
| `keyboard.is_pressed(key)` | 지정한 키가 현재 눌려 있으면 `True` 반환 (루프 내 실시간 감지용) |

```python
import keyboard

# loop() 안에서 ESC 누르면 즉시 정지
if keyboard.is_pressed('esc'):
    kamibot.stop()
    kamibot.close()
```

---

## 🏗️ 전체 코드 구조 예시

### 환경 세팅 (Anaconda Prompt)

```bash
# 가상환경 생성
conda create -n kamibot python==3.11

# 가상환경 활성화 — (base) → (kamibot) 변경 확인
conda activate kamibot

# 패키지 설치
pip install pykamipi
pip install helloai     # AI 기능 사용 시
pip install keyboard
```

---

### 표지판 인식 자율주행 로봇

```python
from helloai import *
from pyKamipi.pibot import *
import keyboard

kamibot = KamibotPi("COM6", 57600)
model   = TMImageModel()
wnd     = Window('main')
camera  = Camera(num=0, crop=True, flip=1)   # 480×480 크롭

def setup():
    model.load_model('C:/model/auto')         # 모델 불러오기

def loop():
    img = camera.read()
    img = img.resize(224, 224)                # 티처블머신 입력 크기
    lbl = model.process(img)                  # 이미지 분류
    print(lbl)

    if lbl == "정지":
        kamibot.stop()
    elif lbl == "앞으로":
        kamibot.go_forward_speed(30, 30)

    wnd.show(img)

    if keyboard.is_pressed('esc'):
        kamibot.stop()
        kamibot.close()

if __name__ == '__main__':
    run()
```

---

### 차선 이탈 없는 자율주행 로봇

```python
from helloai import *
from pyKamipi.pibot import *
import keyboard

kamibot = KamibotPi("COM6", 57600)
model   = TMImageModel()
wnd     = Window('main')
camera  = Camera(num=0, crop=True, flip=1)

def setup():
    model.load_model('C:/model/auto')

def loop():
    img = camera.read()
    img = img.resize(224, 224)
    lbl = model.process(img)
    print(lbl)

    if lbl == "앞으로":
        kamibot.go_forward_speed(30, 30)    # 직진
    elif lbl == "왼쪽":
        kamibot.go_forward_speed(20, 60)    # 좌회전 (왼쪽 느리게)
    elif lbl == "오른쪽":
        kamibot.go_forward_speed(60, 20)    # 우회전 (오른쪽 느리게)

    if keyboard.is_pressed("esc"):
        kamibot.stop()

    wnd.show(img)

if __name__ == '__main__':
    run()
```

---

## 📋 티처블머신 모델 학습 → 파이썬 적용 흐름

```
[Teachable Machine]
  ① 크롬에서 teachablemachine.withgoogle.com 접속
  ② 이미지 프로젝트 → 표준 이미지 모델 선택
  ③ 클래스별 웹캠으로 이미지 데이터 수집 및 학습
  ④ 내보내기: Tensorflow 탭 → Keras → 모델 다운로드
  ⑤ converted_keras.zip 압축 해제
       ├── keras_model.h5
       └── labels.txt

[파일 배치]
  C:\model\auto\
       ├── keras_model.h5
       └── labels.txt

[파이썬 코드]
  model.load_model('C:/model/auto')  ← 폴더 경로 지정
  lbl = model.process(img)           ← 분류 결과 = 클래스명 문자열
```

> ⚠️ 클래스명에 **띄어쓰기 사용 금지** (예: `손있음` ✅ / `손 있음` ❌)

---

## 🔌 하드웨어 연결 순서

```
1. USB 동글(FTDI) → PC에 연결
2. 카미봇파이 로봇 전원 ON (밑면 스위치)
3. 동글 옆 스위치 클릭 → 로봇과 동글을 바짝 붙이기
4. LED 파란색 점등 확인 → 연결 완료
5. 장치관리자 → 포트 → USB Serial Port(COMx) 번호 확인
6. 코드에서 COM 포트 번호 일치 여부 확인
```

---

*참고 자료: 카미봇파이 활용 자율주행 로봇(파이썬) 교육 자료 · AI Classroom (https://aiclassroom.kr/)*

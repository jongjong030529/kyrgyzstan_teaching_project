from pyKamipi.pibot import *
from helloai import *
# 객채생성, 동글 COM 포트 설정 , 통신속도 57600
kamibot = KamibotPi('COM7',57600)

# #kamibot의 led함수는 turn_led(R,G,B)

for i in range(1,255,5):
    kamibot.turn_led(i,0,0)  
    kamibot.delay(0.5)
    kamibot.turn_led(0,i,0)
    kamibot.delay(0.5)

# 카미봇으로 멜로디를 생성해보는 코드 
# melody = [55,55,57,57,55,55,52,55,55,52,52,50,55,55,57,57,55,55,52,55,52,50,52,48]
# for i in melody:
#     kamibot.melody(i,0.5)
# 카미봇 고요한밤, 거룩한밤
# melody = [
#     # 고-요-한 밤 (3박자)
#     (67, 0.6), (69, 0.3), (67, 0.6),   # 고요한
#     (64, 1.2),                           # 밤
#     # 거-룩-한 밤
#     (67, 0.6), (69, 0.3), (67, 0.6),   # 거룩한
#     (64, 1.2),                           # 밤
#     # 주의 천사
#     (74, 0.9), (74, 0.6),               # 주의천
#     (71, 1.2),                           # 사
#     # 높은 곳에
#     (72, 0.9), (72, 0.6),               # 높은
#     (67, 1.2),                           # 곳에
#     # 자비하신
#     (76, 0.9), (76, 0.6),               # 자비
#     (72, 0.6), (72, 0.3), (69, 0.3),   # 하신
#     # 주 나셨네
#     (78, 1.2),                           # 주
#     (74, 0.6), (74, 0.3), (72, 0.3),   # 나셨
#     (67, 1.2),                           # 네
# ]

# for note, duration in melody:
#     kamibot.melody(note, duration)

# BTS - Dynamite 메인 훅 멜로디
# MIDI 음계
# C4=60, D4=62, E4=64, F4=65, G4=67, A4=69, B4=71
# C5=72, D5=74, E5=76, F5=77, G5=79, A5=81

# BTS - Dynamite 메인 훅 멜로디
# (MIDI번호, 박자) → 숫자 리스트로 분리

# notes = [
#     # "Cause I, I, I'm in the stars tonight"
#     74, 74, 72,
#     74, 72, 69,
#     67,
#     69, 67,
#     64,

#     # "So watch me bring the fire"
#     67, 67, 69,
#     67, 64, 62,
#     60,

#     # "set the night alight"
#     62, 64, 65,
#     64, 62,
#     60,

#     # "Shining through the city"
#     72, 72, 74,
#     72, 69, 67,
#     69,

#     # "with a little funk and soul"
#     67, 69, 67,
#     64, 65, 64,
#     62,

#     # "So I'ma light it up like dynamite"
#     60, 62, 64,
#     65, 64, 62,
#     64, 65, 67,
#     69,
# ]

durations = [
    # "Cause I, I, I'm in the stars tonight"
    0.3, 0.3, 0.3,
    0.3, 0.3, 0.3,
    0.6,
    0.3, 0.3,
    0.6,

    # "So watch me bring the fire"
    0.3, 0.3, 0.3,
    0.3, 0.3, 0.3,
    0.6,

    # "set the night alight"
    0.3, 0.3, 0.3,
    0.3, 0.3,
    0.9,

    # "Shining through the city"
    0.3, 0.3, 0.3,
    0.3, 0.3, 0.3,
    0.6,

    # "with a little funk and soul"
    0.3, 0.3, 0.3,
    0.3, 0.3, 0.3,
    0.9,

    # "So I'ma light it up like dynamite"
    0.3, 0.3, 0.3,
    0.3, 0.3, 0.3,
    0.3, 0.3, 0.3,
    1.2,
]

# for note, duration in melody:
#     kamibot.melody(note, duration)

kamibot.close()
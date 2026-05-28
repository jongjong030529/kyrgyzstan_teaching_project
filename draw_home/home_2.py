from pyKamipi.pibot import *

kamibot = KamibotPi('COM3', 57600)

SPEED      = 100
UNIT       = 10   # 집 한 변
WIN_UNIT   = 6    # 창문 한 변 (집보다 작게)
WIN_OFFSET = 2    # 창문을 벽 안쪽으로 들여쓰기

# ① 지붕 (삼각형)
kamibot.turn_left_speed(30, SPEED)
kamibot.move_forward_unit(UNIT, "-l", SPEED)
kamibot.turn_right_speed(120, SPEED)
kamibot.move_forward_unit(UNIT, "-l", SPEED)
kamibot.turn_right_speed(150, SPEED)

# ② 몸체 (사각형)
kamibot.move_forward_unit(UNIT, "-l", SPEED)
kamibot.turn_right_speed(90, SPEED)
kamibot.move_forward_unit(UNIT, "-l", SPEED)
kamibot.turn_right_speed(90, SPEED)
kamibot.move_forward_unit(UNIT, "-l", SPEED)
kamibot.turn_right_speed(90, SPEED)
kamibot.move_forward_unit(UNIT, "-l", SPEED)

# ③ 창문 시작점 이동 (사각형 안쪽 왼쪽 위로 이동)
kamibot.turn_right_speed(90, SPEED)
kamibot.move_forward_unit(WIN_OFFSET, "-l", SPEED)  # 오른쪽으로 들여쓰기
kamibot.turn_right_speed(90, SPEED)
kamibot.move_forward_unit(WIN_OFFSET, "-l", SPEED)  # 아래로 들여쓰기
kamibot.turn_left_speed(90, SPEED)                  # 창문 그릴 방향 정렬

# ④ 창문 (작은 사각형)
for _ in range(4):
    kamibot.move_forward_unit(WIN_UNIT, "-l", SPEED)
    kamibot.turn_right_speed(90, SPEED)

kamibot.close()
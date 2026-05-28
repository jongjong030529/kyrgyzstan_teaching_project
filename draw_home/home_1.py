from pyKamipi.pibot import *

kamibot = KamibotPi('COM3', 57600)

SPEED = 100    # 이동 속도
UNIT  = 10     # 한 칸 단위 (5 unit = 사각형 한 변)

# ① 지붕 (이등변삼각형)
# 출발점: 사각형 왼쪽 위 꼭짓점
kamibot.turn_left_speed(30, SPEED)     # 정면 기준 30° 좌회전 (지붕 방향)
kamibot.move_forward_unit(UNIT, "-l", SPEED)  # 왼쪽 빗변
kamibot.turn_right_speed(120, SPEED)   # 꼭대기에서 우회전 120°
kamibot.move_forward_unit(UNIT, "-l", SPEED)  # 오른쪽 빗변
kamibot.turn_right_speed(150, SPEED)   # 사각형 방향으로 우회전

# ② 몸체 (정사각형) — 오른쪽→아래→왼쪽→위 순서로 복귀
kamibot.move_forward_unit(UNIT, "-l", SPEED)  # 오른쪽 변
kamibot.turn_right_speed(90, SPEED)
kamibot.move_forward_unit(UNIT, "-l", SPEED)  # 아랫변
kamibot.turn_right_speed(90, SPEED)
kamibot.move_forward_unit(UNIT, "-l", SPEED)  # 왼쪽 변
kamibot.turn_right_speed(90, SPEED)
kamibot.move_forward_unit(UNIT, "-l", SPEED)  # 윗변 (시작점 복귀)

kamibot.close()
from pyKamipi.pibot import *
# 객채생성, 동글 COM 포트 설정 , 통신속도 57600
kamibot = KamibotPi('COM3',57600)
for i in range(4):
    kamibot.move_forward_unit(5,"-l",100)
    kamibot.turn_right_speed(90,150)
#카미봇 연결 해제
kamibot.close()

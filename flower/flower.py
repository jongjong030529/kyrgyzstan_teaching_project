from pyKamipi.pibot import *
# 객채생성, 동글 COM 포트 설정 , 통신속도 57600
kamibot = KamibotPi('COM3',57600)
kamibot.draw_arc(10, 50, 1)
for i in range(9):
    #3cm 
    kamibot.draw_arc(3, 60,1)
    #회전각(0~360) 과 스피드(0~255)
    kamibot.turn_right_speed(120,150)
    kamibot.draw_arc(3, 60,1)
    kamibot.turn_left_speed(202,150)
#카미봇 연결 해제
kamibot.close()
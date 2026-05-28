from pyKamipi.pibot import *
from helloai import *
# 객채생성, 동글 COM 포트 설정 , 통신속도 57600
kamibot = KamibotPi('COM7',57600)

for i in range(1,255,5):
    kamibot.turn_led(i,0,0)  
    kamibot.delay(0.5)
    kamibot.turn_led(0,i,0)
    kamibot.delay(0.5)

kamibot.close()
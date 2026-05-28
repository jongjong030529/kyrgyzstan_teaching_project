from pyKamipi.pibot import *

kamibot = KamibotPi('COM8',57600)

# 적색
for i in range(0,255,5):
    kamibot.turn_led(i,0,0)
    kamibot.delayms(10)
for i in range(255,0,-5):
    kamibot.turn_led(i,0,0)
    kamibot.delayms(10)

# 녹색
for i in range(0,255,5):
    kamibot.turn_led(0,i,0)
    kamibot.delayms(10)
for i in range(255,0,-5):
    kamibot.turn_led(0,i,0)
    kamibot.delayms(10)

# 파란색
for i in range(0,255,5):
    kamibot.turn_led(0,0,i)
    kamibot.delayms(10)
for i in range(255,0,-5):
    kamibot.turn_led(0,0,i)
    kamibot.delayms(10)

kamibot.close()
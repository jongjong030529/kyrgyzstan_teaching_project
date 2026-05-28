from pyKamipi.pibot import *

kamibot = KamibotPi("COM8",57600)


#사각형
for i in range(5):
    kamibot.move_forward_unit(5,'-l',100)
    kamibot.turn_right_speed(144,100)

kamibot.close()

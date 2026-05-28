from pyKamipi.pibot import *

kamibot = KamibotPi("COM8",57600)

kamibot.draw_arc(10,50,1)

for i in range(9):
    kamibot.draw_arc(3,60,1)
    kamibot.turn_right_speed(120,150)
    kamibot.draw_arc(3,60,1)
    kamibot.turn_left_speed(202,150)

kamibot.close()
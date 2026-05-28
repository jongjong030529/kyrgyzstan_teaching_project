from pyKamipi.pibot import *

kamibot = KamibotPi("COM8",57600)

for i in range(4):
    kamibot.go_dir_speed("f",10,"f",10)
    kamibot.delay(2)
    kamibot.go_dir_speed("f",10,"b",10)
    kamibot.delay(1.4)

kamibot.stop()

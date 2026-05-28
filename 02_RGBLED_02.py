from pyKamipi.pibot import *

kamibot = KamibotPi('COM8',57600)

kamibot.turn_led(255,0,0)
kamibot.delay(2)
kamibot.turn_led(0,255,0)
kamibot.delay(2)

kamibot.turn_led(255,0,0)
kamibot.delay(2)
kamibot.turn_led(0,255,0)
kamibot.delay(2)

kamibot.turn_led(255,0,0)
kamibot.delay(2)
kamibot.turn_led(0,255,0)
kamibot.delay(2)

kamibot.turn_led(255,0,0)
kamibot.delay(2)
kamibot.turn_led(0,255,0)
kamibot.delay(2)
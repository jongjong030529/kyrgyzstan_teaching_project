from pyKamipi.pibot import *
import keyboard

kamibot = KamibotPi("COM8",57600)

while True:
    if keyboard.is_pressed('up'):
        print('up')
        kamibot.go_dir_speed('f',30,'f',30)
    elif keyboard.is_pressed('down'):
        print('down')
        kamibot.go_dir_speed('b',30,'b',30)
    elif keyboard.is_pressed('left'):
        print('left')
        kamibot.go_dir_speed('f',0,'f',30)
    elif keyboard.is_pressed('right'):
        print('right')
        kamibot.go_dir_speed('f',30,'f',0)
    elif keyboard.is_pressed('q'):
        print('exit')
        kamibot.stop()
        break
    else:
        print('stop')
        kamibot.stop()

kamibot.close()
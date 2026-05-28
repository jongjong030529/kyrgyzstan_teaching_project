from pyKamipi.pibot import*
import keyboard

kamibot = KamibotPi('COM8',57600)

while True:
    left,center,right = kamibot.get_line_sensor()
    proxiLeft,proxiRight = kamibot.get_object_detect()
    print(f"left={left}, center={center}, right={right}")
    
    if proxiLeft > 100 or proxiRight >100:
        kamibot.stop()
    else:
        if center == 1 :
            kamibot.go_forward_speed(30,30)
        elif left == 1:
            kamibot.go_forward_speed(0,30)
        elif right == 1:
            kamibot.go_forward_speed(30,0)

    if keyboard.is_pressed('esc'):
        kamibot.stop()
        break

kamibot.close()
from pyKamipi.pibot import*
import keyboard

kamibot = KamibotPi("COM8",57600)


while True:
    if keyboard.is_pressed('esc'):
        kamibot.stop()
        break
    color = kamibot.get_color_sensor()
    print(f"color = {color}")

    if color == 1:
        kamibot.stop()
    elif color == 3:
        kamibot.turn_right_speed(180,30)
    elif color == 4:
        kamibot.turn_right_speed(90,30)
    else:
        kamibot.go_forward_speed(30,30)
    
kamibot.close()
    
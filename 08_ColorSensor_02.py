from pyKamipi.pibot import*
import keyboard

kamibot = KamibotPi("COM8",57600)


while True:
    if keyboard.is_pressed('esc'):
        kamibot.stop()
        break
    color = kamibot.get_color_elements()
    r,g,b = kamibot.get_color_elements()
    print(f"color = {color}")

    if r>240 and g <50 and b<60:
        kamibot.stop()
    elif r>240 and g>230 and b<60:
        kamibot.turn_right_speed(180,30)
    else:
        kamibot.go_forward_speed(30,30)

kamibot.close()
    
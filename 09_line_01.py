from pyKamipi.pibot import*
import keyboard

kamibot = KamibotPi('COM8',57600)

while True:
    left,center,right = kamibot.get_line_sensor()
    print(f"left={left}, center={center}, right={right}")

    if keyboard.is_pressed('esc'):
        kamibot.stop()
        break

kamibot.close()
from pyKamipi.pibot import*

kamibot = KamibotPi('COM8',57600)

while True:
    left,right = kamibot.get_object_detect()
    print(f"left = {left}, right = {right}")

    if left >10:
        kamibot.stop()
    else:
        kamibot.go_forward_speed(30,30)

kamibot.close()
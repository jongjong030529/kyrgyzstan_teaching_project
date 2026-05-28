from pyKamipi.pibot import*

kamibot = KamibotPi('COM8',57600)

while True:
    left,right = kamibot.get_object_detect()
    print(f"left = {left}, right = {right}")

    if left >100 and right >100:
        kamibot.stop()
    elif left >20 and right >20:
        kamibot.go_forward_speed(30,30)
    elif left >20 and right <10:
        kamibot.go_forward_speed(0,30)
    elif left <10 and right >20:
        kamibot.go_forward_speed(30,0)
    else:
        kamibot.stop()

kamibot.close()
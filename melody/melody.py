from pyKamipi.pibot import *
from helloai import *

kamibot = KamibotPi('COM7', 57600)
kamibot.delay(2)          # 연결 안정화 대기
kamibot.melody(67, 0.5)
kamibot.delay(1)
kamibot.close()
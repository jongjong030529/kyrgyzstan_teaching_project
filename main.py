from pyKamipi.pibot import *
from helloai import *
# 객채생성, 동글 COM 포트 설정 , 통신속도 57600
kamibot = KamibotPi('COM7',57600)
kamibot.turn_led(255,0,0)

wnd = Window('main')
camera = Camera(num=0, crop=True, flip=1)
def loop():
    img = camera.read() # 카메라의 데이터를 읽어오는 함수 
    wnd.show(img)
# if __name__ == '__main__':
#     run()

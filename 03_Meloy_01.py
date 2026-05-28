from pyKamipi.pibot import *

kamibot = KamibotPi('COM8',57600)

melody = [55,55,57,57,55,55,52,55,55,52,52,50,55,55,57,57,55,55,52,55,52,50,52,48]
palyT= [0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,1.5,0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,1.5]

for i,j in zip(melody,palyT):
    kamibot.melody(i,j)
kamibot.close()
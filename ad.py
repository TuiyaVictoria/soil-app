from pymata4 import pymata4
#import matplotlib.pyplot as plt 
#import matplotlib.animation as animation

import time

board = pymata4.Pymata4()

anaolog_pin=A0
digital_pin = 8

board.set_pin_mode_analog_input(anaolog_pin)


while True:
    value, timestamp = board.analog_read(anaolog_pin)
    print(value)
    time.sleep(1)
    #plt.title("Moisture values!!!")
    #plt.plot(value)
    #plt.show()

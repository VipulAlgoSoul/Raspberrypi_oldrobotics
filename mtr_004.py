import numpy as np
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(6,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(25,gpio.IN)
mtr= gpio.PWM(12,5000)
mtr.start(100)

a = np.arange(0,100)
gpio.output(6,gpio.HIGH)

while(1):
    if gpio.input(25):
        print("hai")
    else:
        print("pooy")
    time.sleep(.05)
    #print(i)





    
gpio.output(6,gpio.LOW)

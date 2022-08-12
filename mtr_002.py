import numpy as np
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(6,gpio.OUT)
gpio.setup(12,gpio.OUT)
mtr= gpio.PWM(12,50)
mtr.start(0)

a = np.arange(0,100)
gpio.output(6,gpio.HIGH)

for i in a:
    mtr.ChangeDutyCycle(i)
    time.sleep(.5)
    print(i)
gpio.output(6,gpio.LOW)

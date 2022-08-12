import numpy as np
import time
import RPi.GPIO as gpio
from matplotlib import pyplot as plt

gpio.setmode(gpio.BCM)
gpio.setup(6,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(25,gpio.IN)
mtr= gpio.PWM(12,50)
mtr.start(100)

a = np.arange(0,300)
gpio.output(6,gpio.HIGH)
x=np.zeros(a.size))
y=np.zeros(a.size))

for i in a:
    time.sleep(.05)
    if gpio.input(25):
        print("hsi")
    else:
        print("pooy")
    time.sleep(.05)
    #print(i)
gpio.output(6,gpio.LOW)

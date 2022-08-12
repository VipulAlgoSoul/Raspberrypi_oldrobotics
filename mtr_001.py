import numpy as np
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(6,gpio.OUT)
gpio.setup(12,gpio.OUT)

while(1):
    gpio.output(6,gpio.HIGH)
    gpio.output(12, gpio.HIGH)

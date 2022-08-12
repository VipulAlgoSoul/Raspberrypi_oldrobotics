import numpy as np
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(6,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(25,gpio.IN)
mtr= gpio.PWM(12,50)
time_stamp = time.time()
mtr.start(0)

def speed_of_motor(number):
    global time_stamp
    global speed
    time_now=time.time()
    #if ((number%10)==0):
    speed = 10/(time_now-time_stamp)
    time_stamp= time_now
    print("speed ==>", speed)


def my_call(channel):
    global counter
    counter= counter+1
    print(counter)
    if ((counter%10)==0):
        speed_of_motor(counter)


counter = 0
gpio.add_event_detect(25,gpio.RISING,callback = my_call)

a = np.arange(25,100,5)
gpio.output(6,gpio.HIGH)

for i in a:
    mtr.ChangeDutyCycle(i-1)
    #speed_of_motor(counter)
    time.sleep(2)
    #print(i)
gpio.output(6,gpio.LOW)
print(counter)

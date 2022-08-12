import numpy as np
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

motor_pin_enable =6
motor_pin_run = 12
gpio.setup(motor_pin_enable,gpio.OUT) #left motor enable pin
gpio.setup(motor_pin_run,gpio.OUT) #setting pwm motor forward pin
photo_sensor=25 #setting interrupt recieve pin for photointerrupter(PI)
gpio.setup(photo_sensor,gpio.IN)#setting 25 PI as input
mtr= gpio.PWM(motor_pin_run,50) #
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
gpio.add_event_detect(photo_sensor,gpio.RISING,callback = my_call)

a = np.arange(25,100,5)



for i in a:
    mtr.ChangeDutyCycle(i-1)
    #speed_of_motor(counter)
    time.sleep(2)
    #print(i)
print(counter)

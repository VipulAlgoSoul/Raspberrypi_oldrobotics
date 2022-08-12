import numpy as np
import time
import RPi.GPIO as gpio
from matplotlib import pyplot as plt

#setting 6 as motor enable pin
#setting 12 as motoer run pin
#setting interrupt recieve pin for photointerrupter(PI)
motor_pin_enable =6 
motor_pin_run = 12 
photo_sensor=25 

gpio.setmode(gpio.BCM)

gpio.setup(motor_pin_enable,gpio.OUT)
gpio.setup(motor_pin_run ,gpio.OUT)

gpio.setup(photo_sensor,gpio.IN)
mtr= gpio.PWM(motor_pin_run ,50)

time_stamp = time.time()
time_interval=0
speed=0
counter=0
speed_array=0
time_axis=0
mtr.start(0)

def speed_of_motor():

    global time_stamp 
    global speed
    global time_now
    global time_interval
    global speed_array
    global time_axis
    
    time_now=time.time() 
    time_interval=time_now-time_stamp
    speed = 30/(time_interval)
    time_stamp= time_now
    speed_array=np.append(speed_array,speed)
    time_axis=np.append(time_axis,(0+time_now))
    print("speed ==>", speed,"rpm")
    print("time ineterval==>",time_interval)



def my_call(channel):
    global counter
    counter= counter+1
    print(counter)
    if ((counter%10)==0): #checking for exact 10 counts
        speed_of_motor()

gpio.add_event_detect(photo_sensor,gpio.RISING,callback = my_call)
gpio.output(motor_pin_enable,gpio.HIGH)

while(1):
    mtr.ChangeDutyCycle(100)
    if counter>200:
        break
    
gpio.output(motor_pin_enable,gpio.LOW)
plt.plot(time_axis,speed_array)
plt.show()

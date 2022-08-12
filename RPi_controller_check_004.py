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

#global variable decleration
minimum=50
maximum=100
step=5
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
    #time_axis=np.append(time_axis,(0+time_now))
    time_axis=np.append(time_axis,(counter))
    print("\n speed ==>", speed,"rpm")
    #print("time ineterval==>",time_interval)



def my_call(channel):
    global counter
    counter= counter+1
    print("\n",counter)
    if ((counter%10)==0): #checking for exact 10 counts sampling after counts
        speed_of_motor()

gpio.add_event_detect(photo_sensor,gpio.RISING,callback = my_call)
gpio.output(motor_pin_enable,gpio.HIGH)

#while(1):
 #   mtr.ChangeDutyCycle(40)
  #  if counter>200:
   #     break

pwm =np.arange(minimum,maximum)
for i in pwm:
    
    while(1):
        print("for count",i)
        mtr.ChangeDutyCycle(i)
        if counter>(((i-50)*200)+200):
            print("\n o---",i-50)
            break 
    #print(speed_array)
    #print(speed_array[3:18])
    average_speed= (sum(speed_array[(18*i)+3:(18*i)+18]))/(18-3)
    print("\n average speed =============>",average_speed,"rpm")
    #plt.plot(time_axis,speed_array)
    #plt.show()

    
gpio.output(motor_pin_enable,gpio.LOW)
print(speed_array)
print(speed_array[3:18])
average_speed= (sum(speed_array[3:18]))/(18-3)
#print("average speed =============>",average_speed,"rpm")
#plt.plot(time_axis,speed_array)
#plt.show()

gpio.cleanup()

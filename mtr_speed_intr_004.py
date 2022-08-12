import numpy as np
import time
import RPi.GPIO as gpio

motor_pin_enable =6 #setting 6 as motor enable pin
motor_pin_run = 12 #setting 12 as motoer run pin
photo_sensor=25 #setting interrupt recieve pin for photointerrupter(PI)

gpio.setmode(gpio.BCM)

#setting 6 and 12 run and enable pin sas outputs
gpio.setup(motor_pin_enable,gpio.OUT)
gpio.setup(motor_pin_run ,gpio.OUT)

#setting 25 as input pin
gpio.setup(photo_sensor,gpio.IN)
mtr= gpio.PWM(motor_pin_run ,50)#setting pwm frequency to 50 hz

time_stamp = time.time()#initializing timing

mtr.start(0)#initializing motor pwm with 0 


#defining motor speed calculating function
#the input arguement i scounter value
def speed_of_motor():

    #declaring both time stamp and speed
    #as global variables
    global time_stamp 
    global speed
    
    time_now=time.time() #storing present time value into the time_now
    #varible
    time_interval=time_now-time_stamp
    speed = 30/(time_interval)#speed of 10 slot changes in the encoder disc
    time_stamp= time_now #storing the previous time value to time now
    print("speed ==>", speed,"rpm")
    #print("time ineterval==>",time_interval)

#defining call_back function in case of interrupt
def my_call(channel):
    global counter
    counter= counter+1
    #print(counter)
    if ((counter%10)==0): #checking for exact 10 counts
        speed_of_motor()


counter = 0 #initiallizing counter value to zero

#adding the interrupt function
gpio.add_event_detect(photo_sensor,gpio.RISING,callback = my_call)

#enabling the motor
gpio.output(motor_pin_enable,gpio.HIGH)


while(1):
    mtr.ChangeDutyCycle(100)
    #speed_of_motor(counter)
    print(a)
gpio.output(motor_pin_enable,gpio.LOW)
print(counter)

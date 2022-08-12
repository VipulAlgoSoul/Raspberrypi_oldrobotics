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
sample_count_encoder_holes=10 #int(input("enter the encoder sample count : "))#for sampling
total_count_encoder_holes=20 #int(input("enter the total number of holes in the encoder disc used : "))#total number of encoder holes
prop_gain= 0.5

time_stamp=0
time_interval=0
speed=0
counter=0
error=0
speed_array=[]
error_array=[]
time_axis=0

throttle = 0
set_point = 100

#ratio encoder is the ratio of total encoder holes to sample holes
ratio_encoder =total_count_encoder_holes/sample_count_encoder_holes

mtr.start(throttle)####initial value of motor




def speed_of_motor():

    global time_stamp 
    global speed
    #global time_now
    #global time_interval

    global speed_array
    global time_axis
    global ratio_encoder

    global error
    global error_array
    global set_point

    time_now=time.time() 
    time_interval=time_now-time_stamp
    
    speed = 60/((time_interval)*ratio_encoder)#find in rpm
    
    error=set_point-speed
    print("error in speed of motor",error)
    
    time_stamp= time_now
    
    speed_array=np.append(speed_array,speed)
    error_array=np.append(error_array,error)
    
    time_axis=np.append(time_axis,(0+time_now))
    time_axis=np.append(time_axis,(counter))
    my_controller()
    mtr.ChangeDutyCycle(throttle)
    print("\n speed ==>", speed,"rpm")
    #print("time ineterval==>",time_interval)



def my_call(channel):
    global counter
    global sample_count_encoder_holes
    counter= counter+1
    print("\n",counter)
    if ((counter%sample_count_encoder_holes)==0): #checking for exact 10 counts sampling after counts
        speed_of_motor()

def my_controller():
    global prop_gain
    global error
    global throttle
    global speed
    global set_point
    error=set_point-speed
    print("prop_gain",prop_gain)
    print("error",error)
    correction =prop_gain*error
    print("correction =prop_gain*error",correction )
    #throttle=throttle+correction
    print("throttle=throttle+correction",throttle+correction)
    new_throttle=throttle+correction
    
    if (new_throttle>100):
        print("greater than 100")
        print("new_throttle if",new_throttle)
        throttle=100
        print("new_throttle",throttle)
    elif(new_throttle>0):
        print("less than 100")
        throttle=new_throttle
        print("new_throttle elif",throttle)
    else:
        print("less than 0")
        print("new_throttle else 1",new_throttle)
        throttle=0
        print("new_throttle else 2",throttle)

    

gpio.add_event_detect(photo_sensor,gpio.RISING,callback = my_call)

gpio.output(motor_pin_enable,gpio.HIGH)
#mtr.ChangeDutyCycle(30)
time_stamp = time.time()

#while(1):
 #   my_controller()
  #  mtr.ChangeDutyCycle(throttle)
   # print("h")
    #if counter>1000:
     #   break

my_controller()
mtr.ChangeDutyCycle(throttle)
print("h")
    
    





#print("\n average speed =============>",average_speed_array,"rpm ")   
#gpio.output(motor_pin_enable,gpio.LOW)
#print("speed array ===>",speed_array)
#print("average_speed_array",average_speed_array)
#print("average speed =============>",average_speed,"rpm")
#plt.plot()
#plt.title("average speed vs pwm")
#plt.xlabel("pwm")
#plt.ylabel("average speed in rpm")
#plt.grid(True)
#plt.show()

#gpio.cleanup()

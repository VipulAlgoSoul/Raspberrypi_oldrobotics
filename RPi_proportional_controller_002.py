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
#######################################################################
#changeble global variables

threshold_count=200

sample_count_encoder_holes=5 #int(input("enter the encoder sample count : "))#for sampling

prop_gain= 1

min_throttle=19

set_point = 30

######################################################################

total_count_encoder_holes=20 #int(input("enter the total number of holes in the encoder disc used : "))#total number of encoder holes

time_stamp=0

time_interval=0

speed=0

counter=0

error=0

speed_array=[]

error_array=[]

throttle_array = []

throttle_control_array=[]

time_axis=0

throttle = 0

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
    global prop_gain
    global throttle
    global set_point
    global throttle_array
    global throttle_control_array

    time_now=time.time() 
    time_interval=time_now-time_stamp
    
    speed = 60/((time_interval)*ratio_encoder)#find in rpm
    
    error=set_point-speed
    #print("error in speed of motor",error)
    correction =prop_gain*error
    #print("prop_gain",prop_gain)
    #print("error",error)
    correction =prop_gain*error
    #print("correction =prop_gain*error",correction )
    #print("throttle=throttle+correction",throttle+correction)
    new_throttle=throttle+correction
    throttle_array= np.append(throttle_array,new_throttle)
    
    if (new_throttle>100):
        #print("greater than 100")
        #print("new_throttle if",new_throttle)
        throttle=100
        throttle_control_array = np.append(throttle_control_array,throttle)
        #throttle_array=np.append(throttle_array,throttle)
        #print("new_throttle",throttle)
    elif(new_throttle>=0):
        #print("less than 100")
        throttle=new_throttle
        throttle_control_array = np.append(throttle_control_array,throttle)
        #throttle_array=np.append(throttle_array,throttle)
        #print("new_throttle elif",throttle)
    else:
        #print("less than 0")
        #print("new_throttle else 1",new_throttle)
        throttle=min_throttle
        throttle_control_array = np.append(throttle_control_array,throttle)
        #throttle_array=np.append(throttle_array,throttle)
        #print("new_throttle else 2",throttle)
    time_stamp= time_now
    
    speed_array=np.append(speed_array,speed)
    error_array=np.append(error_array,error)
    
    #time_axis=np.append(time_axis,(0+time_now))
    #time_axis=np.append(time_axis,(counter))

    mtr.ChangeDutyCycle(throttle)
    time_stamp= time_now
    #print("\n speed ==>", speed,"rpm")
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
    global throttle_array
    global min_throttle
    error=set_point-speed
    #print("prop_gain",prop_gain)
    #print("error",error)
    correction =prop_gain*error
    #print("correction =prop_gain*error",correction )
    throttle=throttle+correction
    #print("throttle=throttle+correction",throttle+correction)
    new_throttle=throttle+correction
    #throttle_array= np.append(throttle_array,new_throttle)
    
    if (new_throttle>100):
        #print("greater than 100")
        #print("new_throttle if",new_throttle)
        throttle=100
        #throttle_array=np.append(throttle_array,throttle)
        #print("new_throttle",throttle)
    elif(new_throttle>0):
        #print("less than 100")
        throttle=new_throttle
        #throttle_array=np.append(throttle_array,throttle)
        #print("new_throttle elif",throttle)
    else:
        #print("less than 0")
        #print("new_throttle else 1",new_throttle)
        throttle=min_throttle
        #throttle_array=np.append(throttle_array,throttle)
        #print("new_throttle else 2",throttle)

    

gpio.add_event_detect(photo_sensor,gpio.RISING,callback = my_call)

gpio.output(motor_pin_enable,gpio.HIGH)
#mtr.ChangeDutyCycle(30)
time_stamp = time.time()
my_controller()
while(1):
    my_controller()
    #time.sleep(1)
    mtr.ChangeDutyCycle(throttle)
    #print("throttle adjusted")
    if counter>threshold_count:
        break


gpio.output(motor_pin_enable,gpio.LOW)   
print("gpio lowered")
gpio.cleanup()
s="speed"

print(speed_array)
print(error_array)
print(throttle_array)
print(throttle_control_array)
#print(throttle_array)



size_of_array= speed_array.size
tim_array = np.arange(0,size_of_array)
#print(error_array)
set_point_array = set_point*(np.ones(size_of_array))
plt.plot(tim_array,speed_array,"k")
plt.plot(tim_array,set_point_array)
plt.title("speed transients ""alphabot"" proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("speed in rpm")
plt.grid(True)
plt.show()

plt.plot(tim_array,error_array,"ro")
plt.plot(tim_array,error_array,"r")
plt.plot(tim_array,np.zeros(size_of_array))
plt.title("error variation proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("erro magnitude")
plt.grid(True)
plt.show()


plt.plot(tim_array,error_array,"ro")
plt.plot(tim_array,error_array,"r")
plt.plot(tim_array,np.zeros(size_of_array))
plt.plot(tim_array,throttle_control_array,"b*")
plt.plot(tim_array,throttle_control_array,"b")
plt.title("error variation vs pwm proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("speed in rpm")
plt.grid(True)
plt.show()

plt.plot(tim_array,throttle_array,"r")
plt.plot(tim_array,throttle_array,"ro")
plt.plot(tim_array,throttle_control_array,"b*")
plt.plot(tim_array,throttle_control_array,"b")
plt.title("comparison correction and actual ""alphabot"" proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("pwm applied")
plt.grid(True)
plt.show()

set_point_array = set_point*(np.ones(size_of_array))
plt.plot(tim_array,speed_array,"k")
plt.plot(tim_array,set_point_array)
plt.plot(tim_array,error_array,"ro")
plt.plot(tim_array,error_array,"r")
plt.plot(tim_array,np.zeros(size_of_array))
plt.plot(tim_array,throttle_array,"b")
plt.plot(tim_array,throttle_array,"b*")
plt.plot(tim_array,throttle_control_array,"g^")
plt.plot(tim_array,throttle_control_array,"g")

plt.title("speed transients alphabot proportional controller")
plt.xlabel("time")
plt.ylabel("speed in rpm")
plt.grid(True)
plt.show()




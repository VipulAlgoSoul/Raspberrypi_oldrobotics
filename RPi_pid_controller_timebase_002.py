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

threshold_count=10

sample_count_encoder_holes=5 #int(input("enter the encoder sample count : "))#for sampling

prop_gain= 1

derivative_gain=1

integral_gain = 0.09

min_throttle=18

set_point = 65

######################################################################

total_count_encoder_holes=20 #int(input("enter the total number of holes in the encoder disc used : "))#total number of encoder holes

time_stamp=0

time_interval=0

speed=0

counter=0

error=0

speed_array=[]

error_array=[]
proportional_varied_array=[]

throttle_array = []

throttle_control_array=[]

PID_array = []

integral_error_array=[]
integral_varied_array=[]

differential_error_array=[]
differential_varied_array=[]
time_axis=0

throttle = 0

previous_error=0

differential_error=0

integral_error=0

#ratio encoder is the ratio of total encoder holes to sample holes
ratio_encoder =total_count_encoder_holes/sample_count_encoder_holes

mtr.start(throttle)####initial value of motor




def speed_of_motor():
    global prop_gain
    global derivative_gain
    global integral_gain

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
    
    global throttle
    global set_point
    global throttle_array
    global throttle_control_array
    
    global previous_error
    global integral_error
    global differential_error

    global integral_error_array
    global differential_error_array
    global PID_array

    global integral_varied_array
    global proportional_varied_array
    global differential_varied_array

    prvs_count=0
    no_of_count=0
    no_of_count= counter-prvs_count
    speed = 60*(no_of_count)/total_count_encoder_holes#find in rpm
    
    error=set_point-speed
    proportional_varied_array=np.append(proportional_varied_array,(prop_gain*error))
    #print("error in speed of motor",error)
    differential_error=error-previous_error
    differential_varied_array=np.append(differential_varied_array,(derivative_gain*differential_error))
    previous_error=error

    differential_error_array=np.append(differential_error_array,differential_error)

    integral_error= error+integral_error
    integral_varied_array = np.append(integral_varied_array,(integral_gain*integral_error))

    integral_error_array= np.append(integral_error_array,integral_error)


    ##################################################
    
    correction =(prop_gain*error)+ (derivative_gain*differential_error) + (integral_gain*integral_error)

    PID_array =np.append(PID_array,correction)
    ##################################################
    #print("prop_gain",prop_gain)
    print("error",error)
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
    
    speed_array=np.append(speed_array,speed)
    error_array=np.append(error_array,error)
    
    #time_axis=np.append(time_axis,(0+time_now))
    #time_axis=np.append(time_axis,(counter))

    mtr.ChangeDutyCycle(throttle)
    prvs_count=no_of_count
    time_stamp= time_now
    print("\n speed ==>", speed,"rpm")
    print("time ineterval==>",time_interval)



def my_call(channel):
    global counter
    global sample_count_encoder_holes
    global time_stamp
    global time_now
    time_now = time.time()
    time_interval= time_stamp-time_now
    counter= counter+1
    print("\n","!",counter,"!")
    if (time_interval>=1): #checking for exact 10 counts sampling after counts
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
    print("throttle=throttle+correction",throttle+correction)
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
mtr.ChangeDutyCycle(40)

time_stamp = time.time()
#my_controller()


while(1):
   # my_controller()
    #time.sleep(1)
    mtr.ChangeDutyCycle(throttle)
    print(throttle)
    print("throttle adjusted")
    if counter>threshold_count:
        #gpio.output(motor_pin_enable,gpio.LOW)
        break


gpio.output(motor_pin_enable,gpio.LOW)   
print("gpio lowered")
gpio.cleanup()




print(speed_array)
print(error_array)
print(throttle_array)
print(throttle_control_array)
#print(throttle_array)

#111111111111111111111111111111111111111111111111111111111111
size_of_array= speed_array.size
tim_array = np.arange(0,size_of_array)
#print(error_array)
set_point_array = set_point*(np.ones(size_of_array))
plt.plot(tim_array,speed_array,"k")
plt.plot(tim_array,throttle_control_array,"b*")
plt.plot(tim_array,throttle_control_array,"b")
plt.plot(tim_array,set_point_array)
plt.title("speed transients ""alphabot"" proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("speed in rpm")
plt.grid(True)
plt.show()
#22222222222222222222222222222222222222222222222222222222222
plt.plot(tim_array,error_array,"ro")
plt.plot(tim_array,error_array,"r")
plt.plot(tim_array,np.zeros(size_of_array))
plt.title("error variation proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("erro magnitude")
plt.grid(True)
plt.show()

#33333333333333333333333333333333333333333333333333333333333
plt.plot(tim_array,error_array,"ro")
plt.plot(tim_array,error_array,"r")
plt.plot(tim_array,differential_error_array,"b*")
plt.plot(tim_array,differential_error_array,"b")
plt.plot(tim_array,integral_error_array,"go")
plt.plot(tim_array,integral_error_array,"g")
plt.plot(tim_array,np.zeros(size_of_array))
plt.title("error variation proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("erro magnitude")
plt.grid(True)
plt.show()

#44444444444444444444444444444444444444444444444444444444444
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

#5555555555555555555555555555555555555555555555555555555555555
plt.plot(tim_array,throttle_array,"r")
plt.plot(tim_array,throttle_array,"ro")
plt.plot(tim_array,throttle_control_array,"b*")
plt.plot(tim_array,throttle_control_array,"b")
plt.title("comparison correction and actual ""alphabot"" proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("pwm applied")
plt.grid(True)
plt.show()
#66666666666666666666666666666666666666666666666666666666666666
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

plt.title("speed transients alphabot pid controller")
plt.xlabel("time")
plt.ylabel("speed in rpm")
plt.grid(True)
plt.show()

plt.figure()
plt.subplot(2,3,1)

plt.plot(tim_array,speed_array,"k")
plt.plot(tim_array,set_point_array)
plt.plot(tim_array,throttle_control_array,"b*")
plt.plot(tim_array,throttle_control_array,"b")
plt.title("speed transients & throttle control")
plt.xlabel("time_pseudo")
plt.ylabel("speed in rpm and pwm")
plt.grid(True)

plt.subplot(2,3,2)
plt.plot(tim_array,error_array,"ro")
plt.plot(tim_array,error_array,"r")
plt.plot(tim_array,proportional_varied_array,"bo")
plt.plot(tim_array,proportional_varied_array,"b")
plt.plot(tim_array,np.zeros(size_of_array))
plt.title("prop error variation & prop error controller")
plt.xlabel("time_pseudo")
plt.ylabel("erro magnitude")
plt.grid(True)

plt.subplot(2,3,3)

plt.plot(tim_array,differential_error_array,"r*")
plt.plot(tim_array,differential_error_array,"r")
plt.plot(tim_array,differential_varied_array,"b*")
plt.plot(tim_array,differential_varied_array,"b")

plt.plot(tim_array,np.zeros(size_of_array))
plt.title(" diffrnt error variation controller")
plt.xlabel("time_pseudo")
plt.ylabel("erro magnitude")
plt.grid(True)

plt.subplot(2,3,4)
plt.plot(tim_array,integral_error_array,"r*")
plt.plot(tim_array,integral_error_array,"r")
plt.plot(tim_array,np.zeros(size_of_array))
plt.plot(tim_array,integral_varied_array,"b*")
plt.plot(tim_array,integral_varied_array,"b")
plt.plot(tim_array,np.zeros(size_of_array))
plt.title("integrl error variation & error manipulated")
plt.xlabel("time_pseudo")
plt.ylabel("error magnitude")
plt.grid(True)

plt.subplot(2,3,5)
plt.plot(tim_array,error_array,"ro")
plt.plot(tim_array,error_array,"r")
plt.plot(tim_array,PID_array,"g*")
plt.plot(tim_array,PID_array,"g")
plt.title("comparison correction and actual ""alphabot"" proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("pwm applied")

plt.title("error and pid correction")
plt.xlabel("time")
plt.ylabel("error magnitude")
plt.grid(True)

plt.subplot(2,3,6)
plt.plot(tim_array,throttle_array,"r")
plt.plot(tim_array,throttle_array,"ro")
plt.plot(tim_array,throttle_control_array,"b*")
plt.plot(tim_array,throttle_control_array,"b")
plt.title("comparison correction and actual ""alphabot"" proportional controller")
plt.xlabel("time_pseudo")
plt.ylabel("pwm applied")

plt.title("speed transients alphabot proportional controller")
plt.xlabel("time")
plt.ylabel("speed in rpm")
plt.grid(True)
plt.show()

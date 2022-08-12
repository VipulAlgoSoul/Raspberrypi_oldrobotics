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
sample_count_encoder_holes=int(input("enter the encoder sample count : "))#for sampling
total_count_encoder_holes=int(input("enter the total number of holes in the encoder disc used : "))#total number of encoder holes

minimum= int(input("enter the PWM start value : ")) 
maximum = int(input("enter the PWM end value : "))
step = int(input("enter the step size for PWM increment : "))
count_per_pwm = int(input("enter the count per PWM,(generally 200 and above) : "))

time_stamp=0
time_interval=0
speed=0
counter=0
speed_array=0
time_axis=0
average_speed_array=[]

initial_index=3
final_index=(count_per_pwm/sample_count_encoder_holes)-initial_index


#ratio encoder is the ratio of total encoder holes to sample holes
ratio_encoder =total_count_encoder_holes/sample_count_encoder_holes

mtr.start(0)




def speed_of_motor():

    global time_stamp 
    global speed
    global time_now
    global time_interval
    global speed_array
    global time_axis
    global ratio_encoder
    
    time_now=time.time() 
    time_interval=time_now-time_stamp
    speed = 60/((time_interval)*ratio_encoder) #find in rpm
    time_stamp= time_now
    speed_array=np.append(speed_array,speed)
    #time_axis=np.append(time_axis,(0+time_now))
    time_axis=np.append(time_axis,(counter))
    #print("\n speed ==>", speed,"rpm")
    #print("time ineterval==>",time_interval)



def my_call(channel):
    global counter
    global sample_count_encoder_holes
    counter= counter+1
    #print("\n",counter)
    if ((counter%sample_count_encoder_holes)==0): #checking for exact 10 counts sampling after counts
        speed_of_motor()

gpio.add_event_detect(photo_sensor,gpio.RISING,callback = my_call)
gpio.output(motor_pin_enable,gpio.HIGH)


pwm =np.arange(minimum,maximum,step)
time_stamp = time.time()





for i in pwm:
    #print("for count",i)
    start_index=int((final_index*((i-minimum)/step))+initial_index)
    #print("hi",start_index)
    stop_index=int((final_index*((i-minimum)/step))+final_index)
    #print("pooyy",stop_index)
    while(1):
        
        mtr.ChangeDutyCycle(i)
        if counter> ((i-minimum)/step)*count_per_pwm+count_per_pwm:
            #print("\n o---",i-50)
            break
    #print("values are-----",(final_index*((i-minimum)/step))+initial_index,"\n",(final_index*((i-minimum)/step))+final_index)
    speed_slice= speed_array[start_index:stop_index]   
    average_speed=(sum(speed_slice)/speed_slice.size)
    #print("val__________",value)

    average_speed_array=np.append(average_speed_array,average_speed)
    



#print("\n average speed =============>",average_speed_array,"rpm ")   
gpio.output(motor_pin_enable,gpio.LOW)
#print("speed array ===>",speed_array)
#print("average_speed_array",average_speed_array)
#print("average speed =============>",average_speed,"rpm")
plt.plot(pwm,average_speed_array)
plt.title("average speed vs pwm")
plt.xlabel("pwm")
plt.ylabel("average speed in rpm")
plt.grid(True)
plt.show()

gpio.cleanup()

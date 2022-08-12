import numpy as np
import time

def heart_beat(amplitude, frequency,colour):
    T = 1/frequency #toatl beat time in milliseconds
    #AB
    #static
    pwm =int(amplitude*(0.231))
    time.sleep(T*.238)

    #BC
    #positive increment
    A=0.095
    B=0.231
    C=0.331
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        pwm = i

    #CD
    #negative increment
    A=0.048
    B=0.331
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        pwm = i

   #DE
    pwm =int(amplitude*(0.231))
    time.sleep(T*.071)

    #negative increment
    #EF
    A=0.024
    B=0.231
    C=0.131
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        pwm = i

    #FG
    A=0.024
    B=0.131
    C=1
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        pwm = i

    #GH
    A=0.024
    B=1
    C=0
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        pwm = i

    #HI
    A=0.024
    B=0
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        pwm = i

    #IJ
    #static
    pwm =int(amplitude*(0.231))
    time.sleep(T*.167)
    
    #JK
    A=0.143
    B=0.231
    C=0.385
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        pwm = i

    #KL
    A=0.095
    B=0.385
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        pwm = i

    #LM
    #static
    pwm =int(amplitude*(0.231))
    time.sleep(T*.034)
    

    

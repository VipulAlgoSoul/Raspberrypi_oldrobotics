import numpy as np
import time

#the magnitude value go from B to C
#if the magnitude value increases or decreases B to C then apply threshold
#if B > C then increase section

def heart_beat(amplitude, frequency,colour):
    T = 1/frequency #total beat time in milliseconds
    #AB
    #static
    pwm =int(amplitude*(0.231))
    print(pwm)
    time.sleep(T*.238)

    #BC
    print('bc')
    #positive increment
    A=0.095
    B=0.231
    C=0.331
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = i
        print(pwm)

    #CD
    print('cd')
    #negative increment
    A=0.048
    B=0.331
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = i
        print(pwm)

   #DE
    pwm =int(amplitude*(0.231))
    print(pwm)
    time.sleep(T*.071)

    #negative increment
    #EF
    A=0.024
    B=0.231
    C=0.131
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = i
        print(pwm)

    #FG
    A=0.024
    B=0.131
    C=1
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = i
        print(pwm)

    #GH
    A=0.024
    B=1
    C=0
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = i
        print(pwm)

    #HI
    A=0.024
    B=0
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = i
        print(pwm)

    #IJ
    #static
    pwm =int(amplitude*(0.231))
    print(pwm)
    time.sleep(T*.167)
    
    #JK
    A=0.143
    B=0.231
    C=0.385
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = i
        print(pwm)

    #KL
    A=0.095
    B=0.385
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc) 
    for i in bc:
        pwm = i
        print(pwm)

    #LM
    #static
    pwm =int(amplitude*(0.231))
    print(pwm)
    time.sleep(T*.034)
    


heart_beat(100,80,1)

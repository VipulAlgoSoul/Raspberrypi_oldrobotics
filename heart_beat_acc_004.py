import numpy as np
import time

#the magnitude value go from B to C
#if the magnitude value increases or decreases B to C then apply threshold
#if B > C then increase section

def heart_beat(amplitude, frequency):
    T = 1/frequency #total beat time in milliseconds
    #AB
    #static
    print('entering static section AB')
    pwm =int(amplitude*(0.231))
    print(pwm)
    time.sleep(T*.238)

    #BC
    print('entering incremental section BC')
    #positive increment
    A=0.095
    B=0.231
    C=0.331
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        print(pwm)

    #CD
    print('entering decremental section CD')
    #negative increment
    A=0.048
    B=0.331
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        print(pwm)

   #DE
    print('entering static section DE')
    pwm =int(amplitude*(0.231))
    print(pwm)
    time.sleep(T*.071)

    #negative increment
    print('entering decremental section EF')
    #EF
    A=0.024
    B=0.231
    C=0.131
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        print(pwm)

    #FG
    print('entering incremental section FG')
    A=0.024
    B=0.131
    C=1
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        print(pwm)

    #GH
    print('entering decremental section GH')
    A=0.024
    B=1
    C=0
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm =int(i)
        print(pwm)

    #HI
    print('entering incremental section HI')
    A=0.024
    B=0
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        print(pwm)

    #IJ
    print('entering static section IJ')
    #static
    pwm =int(amplitude*(0.231))
    print(pwm)
    time.sleep(T*.167)
    
    #JK
    print('entering incremental section JK')
    A=0.143
    B=0.231
    C=0.385
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        print(pwm)

    #KL
    print('entering decremental section KL')
    A=0.095
    B=0.385
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        print(pwm)

    #LM
    print('entering static section LM')
    #static
    pwm =int(amplitude*(0.231))
    print(pwm)
    time.sleep(T*.034)
    

heart_beat(100,60)

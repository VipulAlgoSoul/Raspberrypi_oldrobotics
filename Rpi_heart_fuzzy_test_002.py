import numpy as np
import time
import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio.setup(12,gpio.OUT)#green
gpio.setup(13,gpio.OUT)#red
gpio.setup(19,gpio.OUT)#blue
ledg=gpio.PWM(12,10000)
ledg.start(0)
ledr=gpio.PWM(13,10000)
ledr.start(0)
ledb=gpio.PWM(19,10000)
ledb.start(0)

#the magnitude value go from B to C
#if the magnitude value increases or decreases B to C then apply threshold
#if B > C then increase section

def heart_beatg(amplitude, frequency):
    print('start')
    T = 1/frequency #total beat time in milliseconds
    #AB
    #static
    #print('entering static section AB')
    pwm =int(amplitude*(0.231))
    ledg.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.238)

    #BC
    #print('entering incremental section BC')
    #positive increment
    A=0.095
    B=0.231
    C=0.331
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledg.ChangeDutyCycle(pwm)
        print(pwm)

    #CD
    #print('entering decremental section CD')
    #negative increment
    A=0.048
    B=0.331
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledg.ChangeDutyCycle(pwm)
        print(pwm)

   #DE
    #print('entering static section DE')
    pwm =int(amplitude*(0.231))
    ledg.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.071)

    #negative increment
    #print('entering decremental section EF')
    #EF
    A=0.024
    B=0.231
    C=0.131
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledg.ChangeDutyCycle(pwm)
        print(pwm)

    #FG
    #print('entering incremental section FG')
    A=0.024
    B=0.131
    C=1
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledg.ChangeDutyCycle(pwm)
        print(pwm)

    #GH
    #print('entering decremental section GH')
    A=0.024
    B=1
    C=0
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm =int(i)
        ledg.ChangeDutyCycle(pwm)
        print(pwm)

    #HI
    #print('entering incremental section HI')
    A=0.024
    B=0
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledg.ChangeDutyCycle(pwm)
        print(pwm)

    #IJ
    #print('entering static section IJ')
    #static
    pwm =int(amplitude*(0.231))
    ledg.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.167)
    
    #JK
    #print('entering incremental section JK')
    A=0.143
    B=0.231
    C=0.385
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledg.ChangeDutyCycle(pwm)
        print(pwm)

    #KL
    #print('entering decremental section KL')
    A=0.095
    B=0.385
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledg.ChangeDutyCycle(pwm)
        print(pwm)

    #LM
    #print('entering static section LM')
    #static
    pwm =int(amplitude*(0.231))
    ledg.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.034)

def heart_beatr(amplitude, frequency):
    print('start')
    T = 1/frequency #total beat time in milliseconds
    #AB
    #static
    #print('entering static section AB')
    pwm =int(amplitude*(0.231))
    ledr.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.238)

    #BC
    #print('entering incremental section BC')
    #positive increment
    A=0.095
    B=0.231
    C=0.331
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledr.ChangeDutyCycle(pwm)
        print(pwm)

    #CD
    #print('entering decremental section CD')
    #negative increment
    A=0.048
    B=0.331
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledr.ChangeDutyCycle(pwm)
        print(pwm)

   #DE
    #print('entering static section DE')
    pwm =int(amplitude*(0.231))
    ledr.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.071)

    #negative increment
    #print('entering decremental section EF')
    #EF
    A=0.024
    B=0.231
    C=0.131
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledr.ChangeDutyCycle(pwm)
        print(pwm)

    #FG
    #print('entering incremental section FG')
    A=0.024
    B=0.131
    C=1
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledr.ChangeDutyCycle(pwm)
        print(pwm)

    #GH
    #print('entering decremental section GH')
    A=0.024
    B=1
    C=0
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm =int(i)
        ledr.ChangeDutyCycle(pwm)
        print(pwm)

    #HI
    #print('entering incremental section HI')
    A=0.024
    B=0
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledr.ChangeDutyCycle(pwm)
        print(pwm)

    #IJ
    #print('entering static section IJ')
    #static
    pwm =int(amplitude*(0.231))
    ledr.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.167)
    
    #JK
    #print('entering incremental section JK')
    A=0.143
    B=0.231
    C=0.385
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledr.ChangeDutyCycle(pwm)
        print(pwm)

    #KL
    #print('entering decremental section KL')
    A=0.095
    B=0.385
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledr.ChangeDutyCycle(pwm)
        print(pwm)

    #LM
    #print('entering static section LM')
    #static
    pwm =int(amplitude*(0.231))
    ledr.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.034)
    
def heart_beatb(amplitude, frequency):
    print('start')
    T = 1/frequency #total beat time in milliseconds
    #AB
    #static
    #print('entering static section AB')
    pwm =int(amplitude*(0.231))
    ledb.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.238)

    #BC
    #print('entering incremental section BC')
    #positive increment
    A=0.095
    B=0.231
    C=0.331
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledb.ChangeDutyCycle(pwm)
        print(pwm)

    #CD
    #print('entering decremental section CD')
    #negative increment
    A=0.048
    B=0.331
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledb.ChangeDutyCycle(pwm)
        print(pwm)

   #DE
    #print('entering static section DE')
    pwm =int(amplitude*(0.231))
    ledb.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.071)

    #negative increment
    #print('entering decremental section EF')
    #EF
    A=0.024
    B=0.231
    C=0.131
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledb.ChangeDutyCycle(pwm)
        print(pwm)

    #FG
    #print('entering incremental section FG')
    A=0.024
    B=0.131
    C=1
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledb.ChangeDutyCycle(pwm)
        print(pwm)

    #GH
    #print('entering decremental section GH')
    A=0.024
    B=1
    C=0
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm =int(i)
        ledb.ChangeDutyCycle(pwm)
        print(pwm)

    #HI
    #print('entering incremental section HI')
    A=0.024
    B=0
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledb.ChangeDutyCycle(pwm)
        print(pwm)

    #IJ
    #print('entering static section IJ')
    #static
    pwm =int(amplitude*(0.231))
    ledb.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.167)
    
    #JK
    #print('entering incremental section JK')
    A=0.143
    B=0.231
    C=0.385
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i>C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledb.ChangeDutyCycle(pwm)
        print(pwm)

    #KL
    #print('entering decremental section KL')
    A=0.095
    B=0.385
    C=0.231
    inc = ((C-B)*amplitude)/(1000*(A*T))
    bc=np.arange(B*amplitude,C*amplitude+inc,inc)
    #print('size =>',bc.size)
    for i in bc:
        if i<C*amplitude:
            i=C*amplitude
        pwm = int(i)
        ledb.ChangeDutyCycle(pwm)
        print(pwm)

    #LM
    #print('entering static section LM')
    #static
    pwm =int(amplitude*(0.231))
    ledb.ChangeDutyCycle(pwm)
    print(pwm)
    time.sleep(T*.034)

def emot_select(COLOR,amp,freq):
    c=COLOR
    amp=amp
    freq=freq
    if c==1:
        print('green')
        heart_beatg(amp,freq)
        ledg.ChangeDutyCycle(0)
        
    if c==3:
        print('red')
        heart_beatr(amp,freq)
        ledr.ChangeDutyCycle(0)
        
    if c==5:
        print('blue')
        heart_beatb(amp,freq)
        ledb.ChangeDutyCycle(0)
        

emot_select(5,100,40)
emot_select(5,100,42)
emot_select(5,100,40)

emot_select(3,100,10)
emot_select(3,100,10)
emot_select(3,100,10)

emot_select(1,100,15)
emot_select(1,100,15)
emot_select(1,100,15)

gpio.cleanup()

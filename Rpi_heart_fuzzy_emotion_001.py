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

def fuzzy_emotion_(sensor_value):
    val=sensor_value
    if val >0.9:
        #0.9 to 0.1
        print('section two F')
        AMPb = 100
        FREQb = 120
        #C = 5
        return 0,0,0,0,AMPb, FREQb

    elif val >0.8:
          #0.8 TO 0.9
        print('section four A')
        EA=-10*(sensor_value)+9
        AR_L = 100
        AR_H = 0
        FR_L = 120
        FR_H = 60
        AMPr =-1*(AR_H-AR_L)*EA+AR_H 
        FREQr= -1*(FR_H-FR_L)*EA+FR_H
    
        EF=10*(sensor_value)-8
        AB_L = 80
        AB_H = 100
        FB_L = 120
        FB_H = 120
    
        AMPb = (AB_H-AB_L)*EF + AB_L
        FREQb = (FB_H-FB_L)*EF + FB_L

        if AMPr>AMPb:
            return 0,0,AMPr,FREQr,0,0
        else:
            return 0,0,0,0,AMPb,FREQb

    elif val>0.5:
        #0.5 to 0.8
        print('section three A')
        AMPr = 100
        FREQr = 120
        C = 3
        return 0,0,AMPr,FREQr,0,0
    
    elif val>0.4:
        #0.4 to 0.5
        print('section two A')
        EA=5*(sensor_value)-1.5
        AR_L = 90
        AR_H = 100
        FR_L = 90
        FR_H = 120
        C= 3

        AMPr = 2*(AR_H-AR_L)*EA + 80
        FREQr= 2*(FR_H-FR_L)*EA + 60
        return 0,0,AMPr,FREQr,0,0
    
    elif val>0.3:
        #0.3 to 0.4
        print('section three L')
        EL=-10*(sensor_value)+4
        AG_L = 100
        AG_H = 0
        FG_L = 80
        FG_H = 40

        AMPg = -1*(AG_H-AG_L)*EL + AG_H
        FREQg= -1*(FG_H-FG_L)*EL + FG_H

        EA=5*(sensor_value)-1.5
        AR_L = 80
        AR_H = 90
        FR_L = 60
        FR_H = 90
        #C= 3

        AMPr = 2*(AR_H-AR_L)*EA + AR_L
        FREQr= 2*(FR_H-FR_L)*EA + FR_L
    
        if AMPg>AMPr:
            return AMPg,FREQg,0,0,0,0
        else:
            return 0,0,AMPr,FREQr,0,0
    
    elif val>0.2:
        #0.2 to 0.3
        print('section two L')
        AMPg = 100
        FREQg = 80
        #C = 1
        return AMPg, FREQg,0,0,0,0
    
    elif val>0.1:
        #0.1 to 0.2
        print('section one L')
        EL=10*(sensor_value)-1
        AG_L = 80
        AG_H = 100
        FG_L = 60
        FG_H = 80
        C=1

        AMPg = (AG_H-AG_L)*EL + AG_L
        FREQg= (FG_H-FG_L)*EL + FG_L
        return AMPg, FREQg,0,0,0,0
    else:
        #0 to 0.1
        print('section zero')
        AMPg = 80
        FREQg = 60
        Cg = 1
        return AMPg, FREQg,0,0,0,0

    
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

########################################################################
    
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

##########################################################################

def emot_select(AMPg,FREQg,AMPr,FREQr,AMPb,FREQb):
   
    ampg=AMPg
    freqg=FREQg
    ampr=AMPr
    freqr=FREQr
    ampb=AMPb
    freqb=FREQb
    if ampg>0:
        print('green')
        heart_beatg(ampg,freqg)
        ledg.ChangeDutyCycle(0)
        
    if ampr>0:
        print('red')
        heart_beatr(ampr,freqr)
        ledr.ChangeDutyCycle(0)
        
    if ampb>0:
        print('blue')
        heart_beatb(ampb,freqb)
        ledb.ChangeDutyCycle(0)
        
sensor_val = np.arange(0,1,0.025)
count = 0
for i in sensor_val:
    
    ag,fg,ar,fr,ab,fb =fuzzy_emotion_(i)
    emot_select(ag,fg,ar,fr,ab,fb)
    count=count+1


gpio.cleanup()

import time
import RPi.GPIO as gpio
from matplotlib import pyplot as plt
gpio.setmode(gpio.BCM)
gpio.setup(12, gpio.OUT)
led= gpio.PWM(12,10000)
led.start(0)

def EMG_V(freq,ENABLE):
    #freq should change from 0.01,0.005,0.001
    while ENABLE:
        time.sleep(freq)
        #p segment
        for i in range(40,80):
            led.ChangeDutyCycle(i)
            #time.sleep(0.005)
            plt.plot(i)
            plt.show()
            print(i)
        time.sleep(0.001)
        print('peak p')

        for i in range(80,20,-1):
            led.ChangeDutyCycle(i)
            #time.sleep(0.001)
        print('over p')
#time pr
        time.sleep(0.01)
        #dip before qrs
        led.ChangeDutyCycle(0)
        # qrs
        #time.sleep(0.05)
        led.ChangeDutyCycle(100)
        print('qr completed')
        #time.sleep(0.02)
        led.ChangeDutyCycle(0)
        #time.sleep(0.02)
        #st start
        led.ChangeDutyCycle(45)
        #time.sleep(0.01)
        #st
        print('start st')
        for i in range(45,80):
            led.ChangeDutyCycle(i)
           # time.sleep(0.001)
        time.sleep(0.001)

        for i in range(50,45,-1):
            led.ChangeDutyCycle(i)
            #time.sleep(0.001)

        print('end st')

fre= float(input('enter the frequency'))
try:
    EMG_V(fre,0)
except keyboardInterrupt:
    pass
led.stop()
gpio.cleanup()
        

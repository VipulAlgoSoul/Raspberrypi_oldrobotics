import time
#import RPi.GPIO as gpio
#gpio.setmode(gpio.BCM)
#gpio.setup(12, gpio.OUT)
#led= gpio.PWM(12,10000)
#led.start(0)
global x
from matplotlib import pyplot as plt
def EMG_V():
    for i in range(0,5):
        time.sleep(0.01)
        #p segment
        for i in range(40,80):
            x=i
            plt.plot(x)
            plt.show()
            #time.sleep(0.005)
            print(i)
        time.sleep(0.001)
        print('peak p')

        for i in range(80,20,-1):
            #led.ChangeDutyCycle(i)
            x=i
            plt.plot(x)
            plt.show()
            #time.sleep(0.001)
        print('over p')
#time pr
        time.sleep(0.01)
        #dip before qrs
        #led.ChangeDutyCycle(0)
        x=0
        plt.plot(x)
        plt.show()
        # qrs
        #time.sleep(0.05)
        #led.ChangeDutyCycle(100)
        x=100
        plt.plot(x)
        plt.show()
        print('qr completed')
        #time.sleep(0.02)
        #led.ChangeDutyCycle(0)
        x=0
        plt.plot(x)
        plt.show()
        #time.sleep(0.02)
        #st start
        #led.ChangeDutyCycle(45)
        plt.plot(45)
        plt.show()
        #time.sleep(0.01)
        #st
        print('start st')
        for i in range(45,80):
            #led.ChangeDutyCycle(i)
           # time.sleep(0.001)
           x=i
           plt.plot(x)
           plt.show()
        time.sleep(0.001)

        for i in range(50,45,-1):
            #led.ChangeDutyCycle(i)
            x=i
            plt.plot(x)
            plt.show()
            #time.sleep(0.001)

        print('end st')



EMG_V()

#led.stop()
#gpio.cleanup()
        

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
led= GPIO.PWM(12,1000)
led.start(0)

def led_freq_blink(start_c, pwm, jump_increment):
    while 1:
        for duty in range(start_c,pwm+1,jump_increment):
            led.ChangeDutyCycle(duty)
            time.sleep(.05)
            
            print(duty)
        for duty in range(pwm,start_c-1,-jump_increment):
            led.ChangeDutyCycle(duty)
            time.sleep(.05)
            print(duty)
            



pwm = int(input('enter the pwm [bet 0 to 100] amplitude:'))
freq =int(input('enter the frequency:'))
N= int(2*freq*pwm*(0.02))
remainder= int(pwm%N)
start_c= int(0+remainder)

#led_freq_blink(start_c, pwm, N)
#led.stop()
try:
    led_freq_blink(start_c, pwm, N)
except keyboardInterrupt:
    pass
led.stop()
GPIO.cleanup()
    

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)
led= GPIO.PWM(12,1000)
led.start(0)

def led_freq_blink(pwm,):
    while 1:
        for duty in range(0,pwm+1,1):
            led.ChangeDutyCycle(duty)
            time.sleep(.15)
            print(duty)
        for duty in range(pwm,0-1,-1):
            led.ChangeDutyCycle(duty)
            time.sleep(.15)
            print(duty)
            



pwm = int(input('enter the pwm [bet 0 to 100] amplitude:'))


#led_freq_blink(start_c, pwm, N)
#led.stop()
try:
    led_freq_blink(pwm)
except keyboardInterrupt:
    pass
led.stop()
GPIO.cleanup()
    

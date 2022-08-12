import time


def led_fun(amp,osc):
    led_osc=(osc/1000)
    
    while 'true': #true condition checks status of pot
        m=0
        for pwm_amp in range(0,amp):
            time.sleep(led_osc)
            
            m=m+1
            print(pwm_amp,'\t',m)
            #every for loop should have a condition check
            
        for pwm_amp in range(amp,0,-1):
            time.sleep(led_osc)
            
            m=m+1
            print(pwm_amp,'\t',m)
            
    
        

pwm=int(input('the value of amplitude:'))
pwm_osc=int(input('the value of osc:'))
led_fun(pwm, pwm_osc)

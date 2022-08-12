#rectified functio for bright and dimming the led
#2*f*pwm*[t1+t2] = N
#t1 is the time to increment one for loop count
#t2 is the time taken to execute one duty cycle change command
#time being t1+t2 is equated to .02
#pwm is duty cycle change of pwm [0 to 100]
#f is the frequency of oscillation we want to set
#N is the jump count to be icremented

pwm= int(input('enter the duty cycle:'))
f= int(input('enter the frequency:'))
N= int(2*f*pwm*(0.02))

remainder = int(pwm%N)
start_c=int(0+remainder)

for i in range(start_c,pwm+1,N):
    print(i)
for i in range(pwm,start_c-1,-N):
    print(i)

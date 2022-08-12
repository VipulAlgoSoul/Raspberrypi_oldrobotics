import numpy as np



inc1 = ((0.331-0.231)*100)/(238*(1/60))
pc=np.arange((0.331*100),(0.231*100)-inc1,-inc1)
for i in pc:
    print(i)
amplitude = 100
T=1/60
A=0.024
B=1
C=0
inc = ((C-B)*amplitude)/(48*(1/60))
bc=np.arange(B*amplitude,(C*amplitude)+inc,inc) #negative increment
for i in bc:
    pwm = i
    print(pwm)

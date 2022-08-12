import numpy as np
from matplotlib import pyplot as plt


def integral_curve(error):
    x= error.size
    integral_curve = np.zeros(error.size)
    prv=error[0]
    integral_curve[0]=error[0]
    nex=0
    for i in range(1,x):
        integral_curve[i]=prv+error[i]
        prv = integral_curve[i]
    return integral_curve


def differential_curve(error):
    x= error.size
    diff_curve = np.zeros(error.size)
    prv=error[0]
    diff_curve[0]=error[0]
    nex=0
    for i in range(1,x):
        diff_curve[i]=error[i]-prv
        prv = error[i]
    return diff_curve        

def timeplot(array):
    t= np.zeros(array.size)
    for i in range(0,array.size):
        t[i]=i
    return t
        
        
#array_osc= np.array([0,15,30,38,40,45,48,52,49,45,40,38,35,37,39,40,41,42,41])
array_osc= np.array([15,30,40,45,50,55,50,40,35,32,35,40,45,48,45,40,38,38,40,42,41,41,41,41])
time= timeplot(array_osc)
setpoint_1= 40+np.zeros(array_osc.size)

#
kp= 0.001
ki=0.005
kd = 0.02
#

error = setpoint_1-array_osc

p_curve = error
i_curve = integral_curve(error)
d_curve = differential_curve(error)
pid_curve= p_curve+d_curve+i_curve

kp_curve = kp*error
ki_curve = ki*integral_curve(error)
kd_curve = kd*differential_curve(error)

kpid_curve= kp_curve+kd_curve+ki_curve

#plt.plot(time,array_osc,'r')

fig = plt.figure()
plt.title('g')
plt.subplot(2,3,1)
plt.plot(time,array_osc,'b')
plt.plot(time,setpoint_1,'r')
plt.title('oscil')

plt.subplot(2,3,2)
plt.plot(time,error,'b')
plt.plot(time,np.zeros(array_osc.size),'r')
plt.title('error')

plt.subplot(2,3,3)
plt.plot(time,p_curve)
plt.title('proportional')
plt.plot(time,np.zeros(array_osc.size),'r')

plt.subplot(2,3,4)
plt.plot(time,i_curve)
plt.title('integral')
plt.plot(time,np.zeros(array_osc.size),'r')

plt.subplot(2,3,5)
plt.plot(time, d_curve)
plt.title('derivative')
plt.plot(time,np.zeros(array_osc.size),'r')

plt.subplot(2,3,6)
plt.plot(time,pid_curve)
plt.title('pid')
plt.plot(time,np.zeros(array_osc.size),'r')

fig = plt.figure()
plt.subplot(2,3,1)
plt.plot(time,array_osc,'b')
plt.plot(time,setpoint_1,'r')
plt.title('oscil')

plt.subplot(2,3,2)
plt.plot(time,error,'b')
plt.plot(time,np.zeros(array_osc.size),'r')
plt.title('error')

plt.subplot(2,3,3)
plt.plot(time,kp_curve)
plt.title('proportional')
plt.plot(time,np.zeros(array_osc.size),'r')

plt.subplot(2,3,4)
plt.plot(time,ki_curve)
plt.title('integral')
plt.plot(time,np.zeros(array_osc.size),'r')

plt.subplot(2,3,5)
plt.plot(time, kd_curve)
plt.title('derivative')
plt.plot(time,np.zeros(array_osc.size),'r')

plt.subplot(2,3,6)
plt.plot(time,kpid_curve)
plt.title('pid')
plt.plot(time,np.zeros(array_osc.size),'r')
plt.show()



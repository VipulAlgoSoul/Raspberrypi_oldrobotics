import numpy as np
from matplotlib import pyplot as plt
#from led emo characteristics xls
#the value of s changes from 0 to 1
#the value of frequency changes from flx to fhx
#classification into sections

def section_zero(sensor_value):
    #0 to 0.1
    print('section zero')
    AMPg = 80
    FREQg = 60
    Cg = 1
    return AMPg, FREQg,0,0,0,0

def section_one_L(sensor_value):
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

def section_two_L(sensor_value):
    #0.2 to 0.3
    print('section two L')
    AMPg = 100
    FREQg = 80
    #C = 1
    return AMPg, FREQg,0,0,0,0   
    
def section_three_L(sensor_value):
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
    

#def section_one_A(sensor_value):
    #0.3 to 0.4
 #  EA=5*(sensor_value)-1.5
  #  AR_L = 80
   # AR_H = 90
    #FR_L = 60
    #FR_H = 90
    #C= 3

   # AMPr = 2*(AR_H-AR_L)*EA + AR_L
    #FREQr= 2*(FR_H-FR_L)*EA + FR_L
    #return 0,0,AMPr,FREQr,0,0
  
def section_two_A(sensor_value):
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

def section_three_A(sensor_value):
    #0.5 to 0.8
    print('section three A')
    AMPr = 100
    FREQr = 120
    C = 3
    return 0,0,AMPr,FREQr,0,0
  
def section_four_A(sensor_value):
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
        
    

#def section_one_F(sensor_value):
    #0.8 TO 0.9
 #   print('section one F')
  #  EF=10*(sensor_value)-8
    #AB_L = 80
    #AB_H = 100
    #FB_L = 120
    #FB_H = 120
    
    #AMP = (AB_H-AB_L)*EF + AB_L
    #FREQ = (FB_H-FB_L)*EF + FB_L
    #C = 5
    #return C, AMP,FREQ

def section_two_F(sensor_value):
    #0.9 to 0.1
    print('section two F')
    AMPb = 100
    FREQb = 120
    #C = 5
    return 0,0,0,0,AMPb, FREQb
    
def sensor_function(val):
    if val >0.9:
        ag,fg,ar,fr,ab,fb=section_two_F(val)
        return ag,fg,ar,fr,ab,fb

    elif val >0.8:
        #cb,ab,fb=section_one_F(val)
        ag,fg,ar,fr,ab,fb=section_four_A(val)
        return ag,fg,ar,fr,ab,fb

    elif val>0.5:
        ag,fg,ar,fr,ab,fb= section_three_A(val)
        return ag,fg,ar,fr,ab,fb
    
    elif val>0.4:
        ag,fg,ar,fr,ab,fb=section_two_A(val)
        return ag,fg,ar,fr,ab,fb
    
    elif val>0.3:
        ag,fg,ar,fr,ab,fb=section_three_L(val)
        #cr,ar,fr=section_one_A(val)
        return ag,fg,ar,fr,ab,fb
    
    elif val>0.2:
        ag,fg,ar,fr,ab,fb= section_two_L(val)
        return ag,fg,ar,fr,ab,fb
    elif val>0.1:
        ag,fg,ar,fr,ab,fb= section_one_L(val)
        return ag,fg,ar,fr,ab,fb
    else:
        ag,fg,ar,fr,ab,fb=section_zero(val)
        return ag,fg,ar,fr,ab,fb
        
        
        

x_axs= np.arange(0,1,0.05)
mag =np.zeros(x_axs.size)
freq=np.zeros(x_axs.size)
count = 0
for i in x_axs:
    
    ag,fg,ar,fr,ab,fb =sensor_function(i)
    mag[count]=ag+ar+ab
    freq[count] = fg+fr+fb
    count=count+1
    print('new set for sensor val  = ',i)
    print('ag =', ag)
    print('fg =', fg)
    print('ar =',ar)
    print('fr =', fr)
    print('ab =', ab)
    print('fb =',fb)
   

plt.figure(1)
plt.title('characteristic fuzzy curve')
plt.subplot(2,1,1)
plt.xlim(0,1,0.01)
plt.ylabel('amplitude'),plt.xlabel('sensor value')
plt.plot(x_axs,mag)
plt.text(0.2,91,'happy')
plt.text(0.6,91,'angry')
plt.text(0.87,91,'fear')
plt.grid(True)
plt.subplot(2,1,2)
plt.xlim(0,1)
plt.ylabel('frequency'),plt.xlabel('sensor value')
plt.plot(x_axs,freq)
plt.text(0.2,100,'happy')
plt.text(0.6,100,'angry')
plt.text(0.87,100,'fear')
plt.grid(True)
plt.show()
    

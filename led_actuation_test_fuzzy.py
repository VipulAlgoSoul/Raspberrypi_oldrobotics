import numpy as np
#from led emo characteristics xls
#the value of s changes from 0 to 1
#the value of frequency changes from flx to fhx
#classification into sections

def section_zero(sensor_value):
    #0 to 0.1
    print('section zero')
    AMP = 80
    FREQ = 60
    C = 1
    return C,AMP, FREQ

def section_one_L(sensor_value):
    #0.1 to 0.2
    print('section one L')
    EL=10*(sensor_value)-1
    AG_L = 80
    AG_H = 100
    FG_L = 60
    FG_H = 80
    C=1

    AMP = (AG_H-AG_L)*EL + AG_L
    FREQ= (FG_H-FG_L)*EL + FG_L
    return C,AMP,FREQ

def section_two_L(sensor_value):
    #0.2 to 0.3
    print('section two L')
    AMP = 100
    FREQ = 80
    C = 1
    return C,AMP, FREQ   
    
def section_three_L(sensor_value):
    #0.3 to 0.4
    print('section three L')
    EL=-10*(sensor_value)+4
    AG_L = 100
    AG_H = 0
    FG_L = 80
    FG_H = 40
    C=1

    AMP = -1*(AG_H-AG_L)*EL + AG_H
    FREQ= -1*(FG_H-FG_L)*EL + FG_H
    return C,AMP,FREQ

def section_one_A(sensor_value):
    #0.3 to 0.4
    print('section one A')
    EA=5*(sensor_value)-1.5
    AR_L = 80
    AR_H = 90
    FR_L = 60
    FR_H = 90
    C= 3

    AMP = 2*(AR_H-AR_L)*EA + AR_L
    FREQ= 2*(FR_H-FR_L)*EA + FR_L
    return C, AMP,FREQ
  
def section_two_A(sensor_value):
    #0.4 to 0.5
    print('section two A')
    EA=5*(sensor_value)-1.5
    AR_L = 90
    AR_H = 100
    FR_L = 90
    FR_H = 120
    C= 3

    AMP = 2*(AR_H-AR_L)*EA + 80
    FREQ= 2*(FR_H-FR_L)*EA + 60
    return C, AMP,FREQ

def section_three_A(sensor_value):
    #0.5 to 0.8
    print('section three A')
    AMP = 100
    FREQ = 120
    C = 3
    return C,AMP, FREQ
  
def section_four_A(sensor_value):
    #0.8 TO 0.9
    print('section four A')
    EA=-10*(sensor_value)+9
    AR_L = 100
    AR_H = 0
    FR_L = 120
    FR_H = 60
    C= 3

    AMP =-1*(AR_H-AR_L)*EA+AR_H 
    FREQ= -1*(FR_H-FR_L)*EA+FR_H
    return C, AMP,FREQ

def section_one_F(sensor_value):
    #0.8 TO 0.9
    print('section one F')
    EF=10*(sensor_value)-8
    AB_L = 80
    AB_H = 100
    FB_L = 120
    FB_H = 120
    
    AMP = (AB_H-AB_L)*EF + AB_L
    FREQ = (FB_H-FB_L)*EF + FB_L
    C = 5
    return C, AMP,FREQ

def section_two_F(sensor_value):
    #0.9 to 0.1
    print('section two F')
    AMP = 100
    FREQ = 120
    C = 5
    return C,AMP, FREQ
    
def sensor_function(val):
    if val >0.9:
        cb,ab,fb=section_two_F(val)
        return cb,ab,fb

    elif val >0.8:
        cb,ab,fb=section_one_F(val)
        cr,ar,fr=section_four_A(val)
        return cr,ar,fr,cb,ab,fb

    elif val>0.5:
        cr,ar,fr= section_three_A(val)
        return cr,ar,fr
    
    elif val>0.4:
        cr,ar,fr=section_two_A(val)
        return cr,ar,fr
    
    elif val>0.3:
        cg,ag,fg=section_three_L(val)
        cr,ar,fr=section_one_A(val)
        return cg,ag,fg,cr,ar,fr
    
    elif val>0.2:
        cg,ag,fg= section_two_L(val)
        return cg,ag,fg
    elif val>0.1:
        cg,ag,fg= section_one_L(val)
        return cg,ag,fg
    else:
        cg,ag,fg=section_zero(val)
        return cg,ag,fg
        
        
        
while(1):
    val = float(input('enter the val bet 0 to 1  '))  
    #cr,ar,fr =sensor_function(val)
    cr,ar,fr,cb,ab,fb =sensor_function(val)
    print('cr =', cr)
    print('ar =', ar)
    print('fr =',fr)
    print('cb =', cb)
    print('ab =', ab)
    print('fb =',fb)

import numpy as np
from matplotlib import pyplot as plt
#from led emo characteristics xls
#the value of s changes from 0 to 1
#the value of frequency changes from flx to fhx
#classification into sections

def fuzzy_emotion_(sensor_value):
    val=sensor_value
    if val >0.9:
        #0.9 to 0.1
        print('section two F')
        AMPb = 100
        FREQb = 120
        #C = 5
        return 0,0,0,0,AMPb, FREQb

    elif val >0.8:
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

    elif val>0.5:
        #0.5 to 0.8
        print('section three A')
        AMPr = 100
        FREQr = 120
        C = 3
        return 0,0,AMPr,FREQr,0,0
    
    elif val>0.4:
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
    
    elif val>0.3:
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
    
    elif val>0.2:
        #0.2 to 0.3
        print('section two L')
        AMPg = 100
        FREQg = 80
        #C = 1
        return AMPg, FREQg,0,0,0,0
    
    elif val>0.1:
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
    else:
        #0 to 0.1
        print('section zero')
        AMPg = 80
        FREQg = 60
        Cg = 1
        return AMPg, FREQg,0,0,0,0

count = 0
for i in x_axs:
    
    ag,fg,ar,fr,ab,fb =fuzzy_emotion_(i)
    mag[count]=ag+ar+ab
    freq[count] = fg+fr+fb
    count=count+1
 
    

        

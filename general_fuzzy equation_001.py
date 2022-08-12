#fuzzy function== fuzzy fun curve equation

#general eqtion for incremnetal region =>
#var_val = (end_val-start_val)*fuzzy(sensor_val)+start_val

#general decrement
#var_val = -1*(end_val-start_val)*fuzzy(sensor_val)+end_val

def section_zero(sensor_value):
    #0 to 0.1
    print('section zero')
    #for steady state
    AMPg = 80  ##no   variation
    FREQg = 60
    Cg = 1
    return AMPg, FREQg,0,0,0,0

def section_one_L(sensor_value):
    #0.1 to 0.2
    #for increment xx_l ==> starting_point of variable
    #xx_H ==> ending poiint of variable
    print('section one L')
    EL=10*(sensor_value)-1 #equation fuzzy
    AG_L = 80
    AG_H = 100 ##ag and fg are variable parameters
    FG_L = 60
    FG_H = 80
    C=1
#general eqtion for incremnetal region =>
#var_val = (end_val-start_val)*fuzzy_function+start_val
    AMPg = (AG_H-AG_L)*EL + AG_L #scaling along fuzzy
    FREQg= (FG_H-FG_L)*EL + FG_L
    return AMPg, FREQg,0,0,0,0

def section_three_L(sensor_value):
    #0.3 to 0.4
    #decrement section
    
    print('section three L')
    EL=-10*(sensor_value)+4
    AG_L = 100
    AG_H = 0
    FG_L = 80
    FG_H = 40
#general decrement
#var_val = -1*(end_val-start_val)*fuzzy(sensor_function)+end_val
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
    

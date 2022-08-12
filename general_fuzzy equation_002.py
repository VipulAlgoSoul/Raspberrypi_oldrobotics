import numpy as np
from matplotlib import pyplot as plt

#fuzzy function== fuzzy fun curve equation

#general eqtion for incremnetal region =>
#var_val = (end_val-start_val)*fuzzy(sensor_val)+start_val

#general decrement
#var_val = -1*(end_val-start_val)*fuzzy(sensor_val)+end_val

#in steady state give end and start vales as same 


def vip_trapez_fuzzy(selector,start_val,end_val,emot_val):

    if selector==1:
        #shows incremental region
        val = (end_val-start_val)*emot_val+start_val

    elif selector==0:
        #steady state case
        start_val = end_val
        val = (end_val-start_val)*emot_val+start_val

    else:
        val=-1*(end_val-start_val)*emot_val+end_val

    return val
        
        

print(vip_trapez_fuzzy(1,80,100,0.8))

import math 
import random
import numpy as np
import pandas as pd


#Calculate Weight for each parameter in the similarity index
def calculate_weight(ref_val, upper_lim, lower_lim, threshold=0.8):
  w_lower = math.log(threshold)/math.log(1-abs((lower_lim - ref_val)/(ref_val + lower_lim)))
  w_upper = math.log(threshold)/math.log(1-abs((upper_lim - ref_val)/(upper_lim + ref_val)))
  weight = round(math.sqrt(w_lower*w_upper), 2)
  return weight


#Calculate Similarity Index for Individual Params

def calc_PSI_param(param, upper_lim, lower_lim,ref_val, threshold = 0.8):
  w = {'radius': 0.57, 'density': 1.07, 'escape_velocity': 0.70, 'revolution': 0.70, 'surface_gravity': 0.13, 'surface_temperature': 5.58}

  ref_values = {'radius': 1, 'density': 1, 'escape_velocity': 1, 'revolution': 1, 'surface_gravity': 1, 'surface_temperature': 288}
  # print(param.columns[0])
  # col_lower = param.columns[0].lower()
  # print(col_lower)
  if (param.columns[0] in ref_values):
    if pd.isna(ref_val):
        ref_val = ref_values[param.columns[0]]
    if pd.isna(upper_lim) or pd.isna(lower_lim):
        weight = w[param.columns[0]]
    else:
        weight = calculate_weight(ref_val, upper_lim,  lower_lim,  threshold)
  else:
    weight = calculate_weight(ref_val, upper_lim,  lower_lim,  threshold)  
    
  PSI_P = [] 
  
  for i in range(len(param)):
    V = round(math.pow(1-abs((param.iat[i,0] - ref_val)/(ref_val + param.iat[i,0])), weight), 2)
    PSI_P.append(V)
  
  return PSI_P





#function to calculate combined PSI
def SI_intsurf(data):
    SI_intsurf_df = pd.DataFrame()
    n = len(data.columns)
    data.loc[:,'new'] = 1
    for i in range(0,n):
        data.loc[:,'new'] = data.loc[:,'new']*data.iloc[:,i]
    
    data.loc[:,'new'] = pow(data.loc[:,'new'],1/n)
    rounded_value = round(data.loc[:,'new'],2)
    return rounded_value



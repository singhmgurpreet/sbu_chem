#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:07:12 2020

@author: manjitkaur

"""
# This script will automate the cycling specific capacity analysis for 
# data retreieved from the Maccor. This assumes the data is comma delimited.
# If it is not, append the appropriate delimiter in line 15.

#import time library for calculating elapsed time
import time

t_start = time.time()

# import numpy library
import numpy as np

#input active mass in g
active_mass = [0.005]

#generate array from csv file
raw_data = np.array(np.genfromtxt('MV20789-1.094_abridged.txt', skip_header=2));

# long way of obtaining number of rows data_size = np.asarray(raw_data.shape)
# above continueddata_points = data_size[0]

#obtain number of rows
data_points = len(raw_data[:,1])

spec_cap_unc = np.zeros((data_points,1))

spec_cap_cor = np.zeros((data_points,1))

#generate uncorrected specific capacity
for i in range(data_points-1):
    spec_cap_unc[i] = (raw_data[i,5]/active_mass)

for i in range(data_points-1):
    if raw_data[i,10] == 133:
        spec_cap_cor[i] = (raw_data[i,5]/active_mass)
    else:
        spec_cap_cor[i] = 0
    
raw_data = np.hstack((raw_data,spec_cap_unc,spec_cap_cor))

print(data_points)

np.savetxt('output.txt',raw_data)

t_tot = time.time()-t_start

print("%.2f" % t_tot)

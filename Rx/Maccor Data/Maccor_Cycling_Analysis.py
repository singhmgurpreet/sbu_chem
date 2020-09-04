#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  3 12:07:12 2020

@author: manjitkaur

"""
# This script will automate the cycling specific capacity analysis for 
# data retreieved from the Maccor. This assumes the data is comma delimited.
# If it is not, append the appropriate delimiter in line 15.


# import numpy library
import numpy as np

#input active mass in g
active_mass = [0.005]

#generate array from csv file
raw_data = np.array(np.genfromtxt('GS-211-146B.040.csv', delimiter = ',', skip_header=2));

# long way of obtaining number of rows data_size = np.asarray(raw_data.shape)
# above continueddata_points = data_size[0]

#obtain number of rows
data_points = len(raw_data[:,1])

spec_cap_unc = np.zeros((data_points,1))

#generate uncorrected specific capacity
for i in range(data_points-1):
    spec_cap_unc[i] = (raw_data[i,5]/0.005)
    
raw_data = np.hstack((raw_data,spec_cap_unc))
    
print(spec_cap_unc)

# for i in range((data_points)-1):
    
#     raw_data[i,10] = raw_data[i,]/active_mass

print(data_points)

np.savetxt('output.txt',raw_data)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:21:52 2020

@author: manjitkaur
"""
import numpy as np
import matplotlib.pyplot as plt
import time

minimum = 4
maximum = 7
n = minimum
errors = np.zeros((maximum-n,1))
fin_val = np.zeros((maximum-minimum,1))
acc_val_1 = np.full((maximum-minimum,1),3.1415926535)

for k in range(n,maximum):
    t_start = time.time()
    iter_no = 10**n
    rec_no = 100
    run_no = 1
    trajectory = np.zeros((rec_no,run_no))
    acc_val = np.full((rec_no,run_no),3.1415926535)
    for i in range(run_no):
        in_circle = 0
        for j in range(1,iter_no+1):
            x = np.random.rand()
            y = np.random.rand()
            r = np.sqrt(x**2 + y**2)
            if r < 1:
                in_circle = in_circle+1
            if j % (iter_no/rec_no) == 0:
                trajectory[int(j/(iter_no/rec_no))-1,i] = 4*in_circle/(j)
    t_final = time.time()-t_start
    print("%d iterations complete in %d seconds." % (iter_no,t_final))
    diff = np.mean(np.abs(np.subtract(acc_val,trajectory)))*100
    errors[k-minimum,0] = diff
    n = n+1
    fin_val[k-minimum,0] = trajectory[-1,:]
    
plt.plot(fin_val)
plt.plot(acc_val_1)
plt.savefig('sinc.png', dpi = 300)
# plt.xlim([1,6])
# plt.ylim([0,25])

np.savetxt('pi_tst_error_output',errors)
# print(trajectory[0,0])

# test_arr = np.zeros((10,1))
# for jiter in range (1,1000001):
#     if jiter % 100000 ==0:
#         test_arr[int(jiter/100000)-1,0] = 69/jiter

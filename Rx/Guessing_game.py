# -*- coding: utf-8 -*-
"""
Created on Mon May 25 22:59:22 2020

@author: Gurjot2008
"""


import numpy as np
import time

t_start = time.time()

high_range = 50

comp_guess = np.random.randint(1,high_range)

print("Guess an integer between 1 and %d, motherfucker.\n" % (high_range-1))
time.sleep(3)

user_guess = np.random.randint(1,high_range)

print("I guessed %d." %user_guess)
time.sleep(0.5)
end_game = 0
                 
try_counter = 0

while end_game == 0:
    
    user_guess = np.random.randint(1,high_range)
    print("I guessed %d." %user_guess)
    time.sleep(0.5)

    
    if comp_guess == user_guess:
        try_counter = try_counter + 1
        end_game = 1
    else:
        try_counter = try_counter + 1

t_print = 3.5 + (try_counter*0.5)        
t_tot = time.time()-t_start-t_print        

print("Nice job! It only took your dumbass %d tries and %.2f seconds to get it right.\n" % (try_counter,t_tot))        
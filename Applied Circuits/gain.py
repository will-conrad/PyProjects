
from itertools import combinations

import math
kit_resistors = [
    10, 
    12, 
    15, 
    18, 
    22, 
    27, 
    33, 
    39, 
    47, 
    56, 
    68, 
    82, 
    100, 
    120, 
    150, 
    180, 
    220, 
    270, 
    330, 
    390, 
    470, 
    560, 
    680, 
    820, 
    1e3, 
    1.2e3, 
    1.5e3, 
    1.8e3, 
    2.2e3, 
    2.7e3, 
    3.3e3, 
    3.9e3, 
    4.7e3, 
    5.6e3, 
    6.8e3, 
    8.2e3, 
    10e3, 
    12e3, 
    15e3, 
    18e3, 
    22e3, 
    27e3, 
    33e3, 
    39e3, 
    47e3, 
    56e3, 
    68e3, 
    82e3, 
    100e3, 
    120e3, 
    150e3, 
    180e3, 

    220e3, 
    270e3, 
    330e3, 
    390e3, 
    470e3, 
    560e3, 
    680e3, 
    820e3, 
    1e6
]
kit_caps = [
    0.01e-6,
    0.1e-6,
    0.47e-6
]

# Set tolerance and target gain
tolerance = 0.0075

target = 1

solutions = 0

# Function calculates gain from resistor values
def freq(r17, c15, r19, r18):
    return  (r19/r18) * (1 / (4*r17*c15))
def amp(r19, r18):
    return (r18/r19)*4.5

# Iterate through every combination of resistors
for r17 in kit_resistors:
    for r19 in kit_resistors:
        for r18 in kit_resistors:
            for c15 in kit_caps:
                frequ = freq(r17, c15, r19, r18)
                ampl = amp(r19, r18)

                
                if frequ > 1000 and (target - tolerance) <= ampl <= (target + tolerance): # <= (target + tolerance):
                    solutions+=1
                    print(f"r17:{r17}, r18:{r18}, r19:{r19}, c15:{c15}, freq:{frequ}, amp:{ampl}")




print(f"{solutions} Solutions")
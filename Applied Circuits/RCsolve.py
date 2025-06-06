
from itertools import combinations


# def format_resistor(value):
#     if value >= 1_000_000:
#         return f"{value / 1_000_000:.2f} MOhm"
#     elif value >= 1_000:
#         return f"{value / 1_000:.2f} kOhm"
#     else:
#         return f"{value} Ohm"

# # Function to calculate equivalent resistance in series
# def series_resistance(resistors):
#     return sum(resistors)

# # Function to calculate equivalent resistance in parallel
# def parallel_resistance(resistors):
#     return 1 / sum(1 / r for r in resistors)
# # Function to find scalar multiples of resistors
# def find_scalar_multiples(resistor_set, multiple):
#     return tuple(r * multiple for r in resistor_set)

# # Function to check if a given set of resistors exists in the kit
# def is_valid_combination(resistor_set, kit_resistors):
#     return all(resistor in kit_resistors for resistor in resistor_set)

# # Function to find resistor combinations that meet the desired ratio and their multiples
# def find_resistor_combinations(desired_ratio, tolerance):
#     # Iterate through combinations of resistors
#     for n1 in range(1, len(kit_resistors) + 1):
#         for n2 in range(1, len(kit_resistors) + 1):
#             # Get combinations of resistors from the kit for R1 and R2
#             R1_combinations = combinations(kit_resistors, n1)
#             R2_combinations = combinations(kit_resistors, n2)

#             for R1_set in R1_combinations:
#                 for R2_set in R2_combinations:
#                     # Series configuration
#                     R1_series = series_resistance(R1_set)
#                     R2_series = series_resistance(R2_set)
#                     ratio_series = R2_series / R1_series
#                     if (desired_ratio - tolerance) <= ratio_series <= (desired_ratio + tolerance):
#                         difference_series = abs(ratio_series - desired_ratio)
#                         print(f"Series: R1 set = {R1_set}, R2 set = {R2_set}, "
#                               f"R1_eq = {format_resistor(R1_series)}, R2_eq = {format_resistor(R2_series)}, "
#                               f"ratio = {ratio_series:.4f}, difference = {difference_series:.4f}")
#                         # Check scalar multiples for series configuration
#                         for multiple in [10,100,1000]:  # Checking multiples from 2x to 10x
#                             R1_multiple = find_scalar_multiples(R1_set, multiple)
#                             R2_multiple = find_scalar_multiples(R2_set, multiple)
#                             if is_valid_combination(R1_multiple, kit_resistors) and is_valid_combination(R2_multiple, kit_resistors):
#                                 print(f"Scalar multiple {multiple}x: R1 set = {R1_multiple}, R2 set = {R2_multiple}")

#                     # Parallel configuration
#                     R1_parallel = parallel_resistance(R1_set)
#                     R2_parallel = parallel_resistance(R2_set)
#                     ratio_parallel = R2_parallel / R1_parallel
#                     if (desired_ratio - tolerance) <= ratio_parallel <= (desired_ratio + tolerance):
#                         difference_parallel = abs(ratio_parallel - desired_ratio)
#                         print(f"Parallel: R1 set = {R1_set}, R2 set = {R2_set}, "
#                               f"R1_eq = {format_resistor(R1_parallel)}, R2_eq = {format_resistor(R2_parallel)}, "
#                               f"ratio = {ratio_parallel:.4f}, difference = {difference_parallel:.4f}")
#                         # Check scalar multiples for parallel configuration
#                         for multiple in [10,100,1000]:  # Checking multiples from 2x to 10x
#                             R1_multiple = find_scalar_multiples(R1_set, multiple)
#                             R2_multiple = find_scalar_multiples(R2_set, multiple)
#                             if is_valid_combination(R1_multiple, kit_resistors) and is_valid_combination(R2_multiple, kit_resistors):
#                                 print(f"Scalar multiple {multiple}x: R1 set = {R1_multiple}, R2 set = {R2_multiple}")

# # Tolerance value
# tolerance = 0.0
# desired_ratio = 4  # Set your desired ratio here
# find_resistor_combinations(desired_ratio, tolerance)


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
    0.47e-6,
    1e-9,
    0.1e-9,
    0.68e-9,
    0.15e-6,
    6.8e-9,
    1e-6
]
# Set tolerance and target gain
f_tol = 10
Q_tol = 0.0

target_f = 100
target_Q = 0.707

solutions = 0

# Function calculates gain from resistor values
def getFreq(r1, r2, c1, c2):
    tpi = 2 * math.pi
    return 1 / (tpi * math.sqrt(r1*r2*c1*c2))


def getQHP(r1, r2, c1, c2):
    num = math.sqrt(r1*r2*c1*c2)
    dem = r2*c2 + r2*c1
    return num / dem

def getQLP(r1, r2, c1, c2):
    num = math.sqrt(r1*r2*c1*c2)
    dem = r1*c1 + r2*c1
    return num / dem


# Iterate through every combination of resistors
for r1 in kit_resistors[kit_resistors.index(1000):]:
   for r2 in kit_resistors[kit_resistors.index(1000):]: 
        for c1 in kit_caps:
            for c2 in kit_caps:
                freq = getFreq(r1, r2, c1, c2)
                q = getQLP(r1, r2, c1, c2)

                freqOK = (target_f - f_tol) <= freq <= (target_f + f_tol)
                qOK = (target_Q - Q_tol) <= q <= (target_Q + Q_tol)
                if freqOK and qOK:
                    solutions+=1
                    print(f"r1={r1}, r2={r2}, c1={c1}, c2={c2}, freq={freq}, q={q}")




print(f"{solutions} Solutions")
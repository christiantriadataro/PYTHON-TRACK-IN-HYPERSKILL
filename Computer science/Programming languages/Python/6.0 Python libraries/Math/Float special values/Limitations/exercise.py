# Getting back to real numbers, check if the input float is neither an infinity value nor a
# NaN.

# Assign the result to the variable check.

import math

real_number = float(input())
# change the next line
check = math.isfinite(real_number)
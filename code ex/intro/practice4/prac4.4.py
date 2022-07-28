# Write a module on your local computer that contains the constant pi and implementations of these mathematics functions: exp, sin, cos using Maclaurin series. The result should be computed with 9 exact decimal places and rounded to 6 digits after the comma.

# Assume the module you written in the exercise above is put into a file name trig.py (you should upload that module to the system for this exercise). Use that module in order to compute the sum sin(n+1) + cos(n+2) + sin(n+3) + cos(n+4) + ... + sin(n+19) + cos(n+20), and rounded to 6 digits after the comma. Then compare the result with the result using the implementation from math module (also rounded to 6 digits after the comma) 

# For example:
# Input	Result
# 0       Your own implementation:     0.348855
#         Math module implementation:  0.348855
# 2       Your own implementation:     -0.239774
#         Math module implementation:  -0.239774
import math
import trig
n = int(input())
a = "%.6f" % sum([math.sin(n+i) if i % 2 != 0 else math.cos(n+i) for i in range(1, 21)])
b = "%.6f" % sum([trig.sin(n+i) if i % 2 != 0 else trig.cos(n+i) for i in range(1, 21)])
print(f"Your own implementation:     {b} \nMath module implementation:  {a}")

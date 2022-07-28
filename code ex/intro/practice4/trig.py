import math
from decimal import Decimal
def exp(x):
    e_to_x = 0
    for i in range(100):
        e_to_x += x**i/float(Decimal(math.factorial(i)))
    return float("%.6f" % e_to_x)
def sin(x):
    sin_to_x = 0
    for i in range(100):
        sin_to_x += ((-1)**i) * (x**(2*i+1))/float(Decimal((math.factorial(2*i+1))))
    return float("%.6f" % sin_to_x)
def cos(x):
    cos_to_x = 0
    for i in range(100):
        cos_to_x += ((-1)**i * x**(2*i))/float(Decimal(math.factorial(2*i)))
    return float("%.6f" % cos_to_x)

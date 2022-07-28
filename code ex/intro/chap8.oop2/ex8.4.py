
# For a given function, the analytical expressions for the first and second derivatives must be manually coded. 
# However, we could think of inheriting general functions for computing these derivatives numerically, 
# such that the only thing we must always implement is the function itself. 
# To realize this idea, we create a superclass, which is available in a file namely Derivatives.py:

# Make a subclass Sine1 of class FuncWithDerivatives for defining an interface for the sin(x) function. 
# Implement the function __call__ only, and rely on the inherited df and ddf methods for computing the derivatives. 
# Make another subclass Sine2 for sin(x) where you also implement the df and ddf methods using analytical expressions for the derivatives. 
# For example:

# Test	
            # s1 = Sine1()
            # s2 = Sine2()
            # x = math.pi /3
            # print("%.5f %.5f" % (s1(x), s2(x)))
            # print("%.5f %.5f %.5f %.5f" % (s1.df(x), s2.df(x), s1.ddf(x), s2.ddf(x)))
# Result
    # 0.86603 0.86603
    # 0.49999 0.50000 -0.86602 -0.86603
from Derivatives import *
import math

class Sine1(FuncWithDerivatives):
    def __init__(self):
        FuncWithDerivatives.__init__(self)  
    def __call__(self, x):
        return math.sin(x)
    def df(self, x):
        return FuncWithDerivatives.df(self, x)
    def ddf(self, x):
        return FuncWithDerivatives.ddf(self, x)

class Sine2(FuncWithDerivatives):
    def __init__(self):
        pass
        
    def __call__(self, x):
        return math.sin(x)
        
    def df(self, x):
        return math.cos(x)
        
    def ddf(self, x):
        return -math.sin(x)
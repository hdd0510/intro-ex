a = float(input())
r = a
while  r-a**(1/2) > 1e-8:
    r = (r +(a/r))/2    
    
print("%.7f" % r)   

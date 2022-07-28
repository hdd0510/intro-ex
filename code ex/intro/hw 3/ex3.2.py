def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return f(n-1) + 2*f(n-2)

#tính dãy số a0=0 a1=1 a(n)=(a(n-1))+2.a(n-2)
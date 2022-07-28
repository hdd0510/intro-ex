from math import *
def f(n):
    lst = [[]] * (n-1) 
    if n == 1:
        return [[1]]
    for i in range(n):
        lst[n-2].append(int(factorial(n-1)/(factorial(i)*factorial(n-1-i))))
    return f(n-1) + [lst[n-2]]
def display_pascal_triangle(n):
    for i in range(1,n+1):
        print(" "*(n-i), end="")
        print(*f(n)[i-1])

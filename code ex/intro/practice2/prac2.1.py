def is_perfect(n):
    lst = []
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            lst.append(i)
    if n == sum(lst):
        return True
    else: 
        return False
print(is_perfect(6))


a = int(input())
b = int(input())
def get_divisors(n):
    lst=[]
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            lst.append(i)
    return lst
def friendly(a, b):
    m = sum(get_divisors(b))
    n = sum(get_divisors(a))
    if (a == m) and (b == n):
        return 'YES'
    else:
        return 'NO'

#xem 2 số có là số thân thiện không
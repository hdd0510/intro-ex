a = int(input())
def prime_num(k):
    if k<=1:
        return 'not prime'
    elif k == 2:
        return 'prime'
    else:
        for i in range(2, k):
            if k % i == 0:
                return 'not prime'
        return 'prime'
print(prime_num(a))

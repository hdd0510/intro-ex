a = int(input())
def prime_num(k):
    if k<=1:
        return False
    elif k == 2:
        return True
    else:
        for i in range(2, k):
            if k % i ==0:
                return False
        return True
for i in range(2, a-1):
    t = 'Yes' 
    if (prime_num(i) and prime_num(a-i)) is True:
        break
    else:
        t = 'NO'
print(t)
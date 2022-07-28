def print_prime(n):
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
    a = []
    for i in range(1, n+1):
        if prime_num(i) == True:
            a.append(i)
    b=" ".join(str(k) for k in a)
    return b
print(print_prime(21)) 

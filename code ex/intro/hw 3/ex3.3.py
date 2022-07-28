

def reverse(n):
    b = []
    for i in n:
        b.append(i)
    x ="".join([str(i) for i in b[::-1]])
    return x

#đảo ngược 1 số
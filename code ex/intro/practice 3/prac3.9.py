def transform(l):
    for i in range(len((l))):
        if l[i] % 2 == 0:
            l[i] *= 2
        else:
            l[i] = -l[i]
    return l
print(transform([32, 56, 99, -40, 20, 78, 43, -61, 61]))
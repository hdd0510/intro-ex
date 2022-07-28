a = int(input())
b = int(input())
def sum_digit(a):
    b = len(str(a))
    s = 0
    for i in range(0, int(b)):
        u = str(a)[i]
        s += int(u)
    return s
def sum_ditgit_greater(a, b):
    if sum_digit(a)>sum_digit(b):
        print("YES")
    else:
        print('NO')
sum_ditgit_greater(a, b)




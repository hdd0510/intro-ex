n = int(input())
lst = list(map(int,input().split()))
def L(lst, i, d):
    if i in d:
        return d[i]
    else:
        res = 1
        for j in range(0, i):
            if abs(lst[j]) < abs(lst[i]) and (lst[i])*(lst[j]) == -abs((lst[i])*(lst[j])):
                res = max(res, L(lst, j, d) + 1)
        d[i] = res
    return res
def longest_sub(lst):
    a = 0
    d = {0:1}
    for i in range(len(lst)):
        a = max(a, L(lst, i, d))
    return a
print(longest_sub(lst))   
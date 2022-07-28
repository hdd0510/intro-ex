tmp = input().split(' ')
m, n = int(tmp[0]), int(tmp[1])
for i in range(m):
    for j in range(n*i+1, n*(i+1) + 1):
        print(j, end= " ")
    print()
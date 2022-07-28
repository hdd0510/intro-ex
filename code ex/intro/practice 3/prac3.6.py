temp = input().split(' ')
m, n = int(temp[0]), int(temp[1])

a = []
b = []
for i in range(m):
  a.append(input().split(' '))
for i in range(m):
  b.append(input().split(' '))
for i in range(m):
    for j in range(n):
        print(int(a[i][j]) + int(b[i][j]), end=" ")
    print()    
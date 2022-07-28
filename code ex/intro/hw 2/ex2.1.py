#C1
n = input()
a = len(n)
r = int(n)
q = 0
for i in range(a-1,-1,-1):
  x = 10**i
  t = int(r/x)
  q = q + t
  r = r - t*x
print(q)

#C2
a = input()
b = len(a)
s = 0
for i in range(0, b):
    u = a[i]
    s += int(u)
print(s)


#tổng các chữ số trong 1 số
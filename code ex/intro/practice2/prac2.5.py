def fibo(n, d):
  if n in d:
    return d[n]
  else:
    d[n] = fibo(n-1, d) + fibo(n-2, d)
    return d[n]
d = {1:1, 2:1}
print(fibo(12, d))
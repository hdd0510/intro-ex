n = int(input())
x =2*n-1
for i in range(1,x-1,2):
  print(' '*(int((x-i)/2))+'*'*i+' '*(int((x-i)/2)))
for j in range(x,0,-2):
  print(' '*(int((x-j)/2))+'*'*j+' '*(int((x-j)/2)))
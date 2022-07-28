arr = list(map(int, input().split()))
a = []
x = arr[0]
for i in range(1, len(arr)):
    if arr[i] > x: 
        a.append(arr[i])
    x = arr[i]
if len(a) == 0:
    print('NONE')
print(*a)    

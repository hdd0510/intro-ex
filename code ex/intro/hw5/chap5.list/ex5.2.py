n = int(input())
arr = list(map(int, input().split()))
x = int(input())
a = abs(arr[0] - x)
for i in range(1, len(arr)):
    if abs(arr[i] - x) <= a:
        a = abs(arr[i] - x)
        b = arr[i]
print(b)


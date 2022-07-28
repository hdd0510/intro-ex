a = eval(input())
b = eval(input())
count = 0
for i in a:
    x, y = i
    for k in b:
        if (x, y) == k or (y, x) == k:
            count += 1
print(count)
text = []
lst = []
res = {}
while True:
    try:
        text.append(input())
    except:
        break
for i in text:
    lst.append(i.split())
for i, j in lst:
    if i not in res:
        res[i] = int(j)
    else:
        res[i] += int(j)
for i, j in sorted(list(res.items())):
    print(i, j)
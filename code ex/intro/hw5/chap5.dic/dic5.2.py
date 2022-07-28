text = []
res = {}
while True:
    try:
        text.append(input())
    except:
        break
lst = [j for i in text for j in i.split()]
for ele in lst:
    if ele not in res:
        res[ele] = 0
    else:
        res[ele] += 1
a = (list(sorted(res.items())))
a.sort(key= lambda x: x[1], reverse = True)
for i in a:
    print(i[0])
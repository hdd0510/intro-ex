text = []
res = {}
while True:
    try:
        text.append(input())
    except:
        break
lst = [i for j in text for i in j.split()]
for i in lst:
    if i not in res:
        res[i] = 0
        print(0, end= " ")
    else:   
        res[i] += 1
        print(res[i], end= " ")
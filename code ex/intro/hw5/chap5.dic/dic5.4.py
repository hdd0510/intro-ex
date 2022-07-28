#Bài tìm đời thứ n của 1 người trong phả hệ
n = int(input())
fam = {}
child = []
lst = []
for x in range(n-1):
    a, b = input().split()
    if b not in fam:
        fam[b] = []
    fam[b].append(a)
    child.append(a)
for i in fam:
    if i not in child:
        thayongnoi = i
        lst.append([i, 0])
def gethigh(person, height):
    for i in fam[person]:
        lst.append([i, height + 1])
        if i not in fam:
            continue
        gethigh(i, height + 1)
gethigh(thayongnoi, 0)
lst.sort()
for i in lst:
    print(*i)


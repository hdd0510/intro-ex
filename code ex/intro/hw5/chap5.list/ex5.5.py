n = int(input())
for i in range(n):
    coor = [list(map(int, input().split())) for b in range(8)]
    a = 0
    for j in range(8):
        for k in range(j+1, 8):
            if coor[j][0] == coor[k][0] or coor[j][1] == coor[k][1] or abs((coor[j][0] - coor[k][0])/(coor[j][1] - coor[k][1])) == 1:
                print("YES")
                a = 1
                break
        if a == 1:
            break
    print("NO") if a == 0 else None
    

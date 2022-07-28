def pascal_triangle(n):
    lst = []  
    for i in range(1, n+1):
        lst.append([1]*(i))
    print(1)
    print(str(1) + " " + str(1))
    for i in range(2, n):
        for j in range(1,i):
            lst[i][j] = lst[i-1][j-1]+lst[i-1][j] 
        print(" ".join((map(str, lst[i]))))
pascal_triangle(7)

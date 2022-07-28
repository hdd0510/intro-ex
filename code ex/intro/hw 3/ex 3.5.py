def floyd(n):
    for i in range(1, n+1):
        for j in range(i, 0, -1):
            if j % 2 != 0:
                print(1, end="")
            if j % 2 == 0:
                print(0, end="")
        print()
"""
vẽ hình floyd 1
                 01
                 101
                 0101
                 10101
                 ......
"""
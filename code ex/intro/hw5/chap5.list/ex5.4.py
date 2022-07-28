N, K = map(int, input().split())
a = [list(map(int, (input().split()))) for i in range(K)]
row = ["I"] * N
for pair in a:
    for i in range(pair[0], pair[1] + 1):
        row[i-1] = "."
print("".join(row))
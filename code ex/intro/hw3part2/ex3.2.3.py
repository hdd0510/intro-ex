def hanoi_tower(n):
    if n == 1:
        return 1
    return hanoi_tower(n-1) + 1
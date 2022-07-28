def move(n, a, c, b):
   if n > 0:
        move(n-1, a, b, c)
        print(f"move {a} -> {c}")
        move(n-1, b, c, a)
move(3, 'A', 'C', 'B')


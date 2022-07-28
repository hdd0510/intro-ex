def  sum_and_count(inp):
    a = []
    b = []
    for i in inp:
        if isinstance(i, int):
            a.append(i)
            b.append(1)
        else:
            a.append(sum(i))
            b.append(len(i))
    return [a,b]

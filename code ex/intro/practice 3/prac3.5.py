def remove_duplicates(l):
    x = l[0]
    lst = [x]
    for i in range(1, len(l)):
        if l[i] != x:
            lst.append(l[i])
        x = l[i]
    return lst
print(remove_duplicates([1, 0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4, 5, 5]))
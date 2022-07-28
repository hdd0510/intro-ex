def remove_duplicates(lst):
    a = []   
    for i in lst:
            if lst.count(i) <= 1:
                a.append(i)
    return a
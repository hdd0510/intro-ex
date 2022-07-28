
def sort_students(tup):
    leng = len(tup)
    for i in range(0, leng):
         
        for j in range(i+1, leng):
            if (tup[i][1] > tup[j][1]):
                a = tup[i]
                tup[i] = tup[j]
                tup[j] = a
            elif tup[i][1] == tup[j][1]:
                if tup[i][0] > tup[j][0]:
                    b = tup[i]
                    tup[i]= tup[j]
                    tup[j]= b
    return tup
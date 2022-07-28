def merge_dict(d1, d2):
    for i in d2:
        if i in d1:
            d1[i] += d2[i]
        else:
            d1[i] = d2[i]
    d = d1.items()
    return dict(d)
print(merge_dict({'a': 4, 'b': 2, 'c': 1, "d": 3}, {'b': 3, 'c': 2, 'd': 1, "e": 3, "g": 5}))
#cach 2:
# def merge(a,b) -> dict:
#     res = {**a, **b}
#     print(res)
#     for x in res:
#         if x in a and x in b:
#             res[x] = 0
#             res[x] = a[x] + b[x]
#         else:
#             continue
#     return res


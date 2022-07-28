#def closest_tuple(tuple_list, query, k):
#    tuple_list.append(query)
#    tuple_list.sort(key = lambda x: x[2])
#   a = tuple_list.index(query)
#    if tuple_list[a+1][2] - query[2] < query[2] - tuple_list[a-1][2]:
#        return tuple_list[a+1]
#    else:
#        return tuple_list[a-1]
        
def closest_tuple(tuple_list, query, k):
    a = min(range(len(tuple_list)), key= lambda x: abs(tuple_list[x][k-1] - query[k-1]))
    return tuple_list[a]
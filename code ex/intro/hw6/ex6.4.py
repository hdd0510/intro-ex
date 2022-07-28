#đếm số từ có trong 1 file cho trước(data1.inp                                                                                                                                                                                                                                                                                                          b                        )
def count_words(filepath):
    with open(filepath,'r') as f:
        data = f.read()
    new = data.split()
    return len(new)
file = 'data1.inp'
print(count_words(file))

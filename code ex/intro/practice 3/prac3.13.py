
def vector_distance(v1, v2, **kwargs):
    def dot(v1,v2):
        return sum(v1[i]*v2[i] for i in range(len(v1)))
    for a, b in kwargs.items():
        if b == "manhattan":
            return sum(abs(v1[i] - v2[i]) for i in range(len(v1)))
        elif b == "cosine":
            return  "%.9f" %  ((dot(v1, v2)) / (((dot(v1, v1)))**(1/2) * (dot(v2, v2))**(1/2)))
    return "%.1f" % sum(((v1[i] - v2[i])**2) for i in range(len(v1)))**(1/2)
print(vector_distance([1, 2], [4, 6]))
      

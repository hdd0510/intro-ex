def mirror(s):
    lst = []
    for i in range(len(s)-1, -1, -1):
        if s[i] == "d":
            lst.append("b")
        elif s[i] == "b":
            lst.append("d")
        elif s[i] == "q":
            lst.append("p")
        elif s[i] == "p":
            lst.append("q")
        elif s[i] in list("iovwx"):
            lst.append(s[i])
        else: 
            return "NOT POSSIBLE"    
    return  "".join(lst)     
print(mirror("void"))
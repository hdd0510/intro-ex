s = input()
a =s.split("_")
lst = []
for i in a:
    x = i.capitalize()
    lst.append(x)
print("".join(lst))
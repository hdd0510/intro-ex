import string
n = int(input())
s = input()
alphabet = string.ascii_lowercase
lst = []
for i in s:
    if i.isupper:
        i = i.lower()
    if i == " ":
        lst.append(i)
    else:
        a = (alphabet.find(i) + n) % 26
        lst.append(alphabet[a])
        
print("".join(map(str, lst)))

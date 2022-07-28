n = int(input())
for i in range(1, n+1):
    print("_"*(n-i) + "/" + " "*(2*i-2) +"\\" +"_"*(n-i))
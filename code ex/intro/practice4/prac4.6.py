# Read 2 same-length lists of numbers and write both lists into a file using module pickle. Then load the 2 lists from that file and print the result list which is the index-wise summation of 2 lists

# For example:

# Input	  Result
# 1 2 3   [5, 7, 9]
# 4 5 6
import pickle
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
with open("lists.pkl", "wb") as f:
    pickle.dump((a,b), f)
with open('lists.pkl', 'rb') as f:
    c, d = pickle.load(f)
f.close()
result = [i + j for i, j in zip(c, d)]
print(result)

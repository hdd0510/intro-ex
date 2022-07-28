# Write a program to count the frequency of words from test.inp (already uploaded to the system) and write the string representation of the dictionary of frequency to the file test.out
# Example:
# Content of test.inp:

# A boy walks into the classroom
# A girl runs into the classroom, too
# Then the teacher comes into the classroom

# Content of test.out:

# {'A': 2, 'boy': 1, 'walks': 1, 'into': 3, 'the': 4, 'classroom\n': 1, 'girl': 1, 'runs': 1, 'classroom,': 1, 'too\n': 1, 'Then': 1, 'teacher': 1, 'comes': 1, 'classroom': 1}


with open('test.inp') as f:
    lines = []
    for line in f:
        lines.append(line.split(" "))
    words = [item for sublist in lines for item in sublist]
res = {}
for x in words:
    if x not in res:
        res[x] = 1
    else:
        res[x] += 1
with open("test.out", "w") as f:
    f.write(str(res))
with open('test.out', 'r') as f:
	all = f.read()
	print(all)

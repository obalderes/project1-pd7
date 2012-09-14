#put names into a list
with open('ml7-student-names', 'r') as f:
    names = [line.strip() for line in f]

#seperate by period
p6 =[]
p7 =[]

for name in names:
    if name[-1] == "6":
        p6.append(name)
    else:
        p7.append(name)

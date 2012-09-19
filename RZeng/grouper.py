import random

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

#shuffle lists
random.shuffle(p6)
random.shuffle(p7)

#print in groups of 4
print "\nPERIOD 6:\n"
x = 0
for name in p6:
    if x == 4:
        print ""
        x = 0
    print name
    x = x+1

print "\nPERIOD 7:\n"
x = 0
for name in p7:
    if x == 4:
        print ""
        x = 0
    print name
    x = x+1
 



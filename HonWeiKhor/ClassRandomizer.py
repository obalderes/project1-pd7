import random
f = open('../ml7-student-names')
students_6 = []
students_7 = []

def order(a):
    s = a[0:]
    lname = s[0:s.find(',')]
    s = s[1+s.find(','):]
    fname = s[0:s.find(',')]
    s = s[1+s.find(','):]
    pd = int(s)
    if (pd == 6):
        students_6.append([lname, fname])
    else:
        students_7.append([lname, fname])

def dosplittythings(s):
    a = s[0:]
    returnval = []
    while (len(a) > 4):
        c = []
        b = random.sample(range(len(a)),4)
        b.sort()
        b.reverse()
        for i in b:
            c.append(a.pop(i))
        returnval.append(c)
    if (len(a)>0):
        returnval.append(a)
    return returnval

for line in f:
#    print(line)
    order(line)
groups_6 = dosplittythings(students_6)
groups_7 = dosplittythings(students_7)
print groups_6
print groups_7
raw_input("Press the Enter key to exit.")

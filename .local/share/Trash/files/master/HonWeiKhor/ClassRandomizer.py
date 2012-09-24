import random
f = open('../ml7-student-names')
#global list vars for class list
students_6 = []
students_7 = []

#segregates student data lists [last, first] into appropriate class lists
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

#takes groups of 4 students until < 4 students unchosen
def dosplittythings(s):
    a = s[0:]
    returnval = []
    while (len(a) > 4):
        c = []
        b = random.sample(range(len(a)),4)
        b.sort()#sort so i can reverse
        b.reverse()#reverse because I want to take out largest element first, array list remove logic
        for i in b:
            c.append(a.pop(i))
        returnval.append(c)
    if (len(a)>0):
        returnval.append(a)
    return returnval

#makes output file categorizing groups into period number, group number, and group members
def makeoutputfile(b):
    g = open("./ml7-student-groups","w")
    for a in range(0,len(b)):
        g.write("PERIOD "+str(a+6)+":\n")
        for i in range(0, len(b[a])):
            g.write("  Group "+str(i+1)+":\n")
            for j in range(0, len(b[a][i])):
                g.write("    "+b[a][i][j][1]+" "+b[a][i][j][0]+"\n")

for line in f:
    order(line)
groups_6 = dosplittythings(students_6)
groups_7 = dosplittythings(students_7)
makeoutputfile([groups_6, groups_7])

import random

def genList(filename):
    f = open(filename).read()
    f = f.replace("*REDO*", "")
    f = f.replace("\n", ",")
    print f
    s = process(f)
    return s

def process(f):
    fname, lname, period = "", "", ""
    routine = [lname, fname, period]
    index = 0
    names6, names7 = [],[]
    for c in f:
        f.replace(c, "", 1)
        if c != ",":
            routine[index] += c
        else:
            if routine[index] == "6":
                names6.append(routine[1] + ' ' + routine[0])
                routine = ["", "", ""]
                index = 0
            elif routine[index] == "7":
                names7.append(routine[1] + ' ' + routine[0])
                routine = ["", "", ""]
                index = 0
            else:
                index += 1
    return [names6, names7]

def getRandomGroups(names, members):
    groups = []
    groupsnum = len(names)/members
    for n in range(groupsnum):
        s = ""
        for i in range(members):
            index = random.randrange(0, len(names))
            s += names[index] + ", "
            names.pop(index)
        groups.append(s)
    if names != []:
        s = ""
        for name in names:
            s += name + ", "
        groups.append(s)
    return groups

names = genList("ml7-student-names")
print "Period 6: ", getRandomGroups(names[0], 4)
print "Period 7: ", getRandomGroups(names[1], 4)


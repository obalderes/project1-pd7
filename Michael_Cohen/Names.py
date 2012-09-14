import random

def genList(filename):
    f = open(filename).read()
    f.strip(",6")
    f.strip(",7")
    s = process(f)
    return s

def process(f):
    fnames, lnames = [], []
    s = ""
    for last in f:
        if last != ",":
            s += last
        else:
            f = f[(f.index(last) + 1):]
            lnames += s
            s = ""
            for first in f:
                if first != "\n":
                    s += first
                else:
                    f = f[(f.index(first) + 1):]
                    fnames += s
                    s = ""
                    break
    names = []
    for n in fnames:
        name = n + " " + lnames[0]
        lnames.pop(0)
        names += name
    return names

def getRandomGroups(names, members):
    groups = []
    groupsnum = len(names)/members
    for n in range(groupsnum):
        indeces = random.randrange(0, len(names))
        s = ""
        for index in indeces:
            s += names[index] + ", "
        groups += s
        for index in indeces:
            names.pop(index)
    if names != []:
        s = ""
        for name in names:
            s += name + ", "
        groups += s
    return groups

print getRandomGroups(genList("ml7-student-names"), 4)
            

#this solution is probably much more complicated than is necessary

from random import randrange

names = []
#morenames = {}

f = open('ml7-student-names')

for line in f.readlines():
    names.append(line.strip())

f.close()

pd6 = []
pd7 = []

#print names[5:13]

for name in names:
    if name not in pd6 and name not in pd7:
        if '6' == name[-1]:
            pd6.append(name)
        else: pd7.append(name)

print len(pd6),len(pd7)

groups6 = []
groups7 = []

while len(pd6) > 0:
    group = []
    while len(group) < 4:
        name = pd6[randrange(0,len(pd6))]
        group.append(name)
        pd6.remove(name)
    groups6.append(group)

while len(pd7) > 0:
    group = []
    while len(group) < 4:
        name = pd7[randrange(0,len(pd7))]
        group.append(name)
        pd7.remove(name)
    groups7.append(group)

print groups6[3]

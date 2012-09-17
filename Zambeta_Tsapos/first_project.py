import random
pdSix = list()
pdSeven = list()
pd7Groups = list()
pd6Groups = list()
for line in open("ml7-student-names", "r").readlines():
    name = line.strip().split(",")
    if name[2] == 7:
       pdSeven.append(name)
    else:
        pdSix.append(name)
counter7 = len(pdSeven)
counter6 = len(pdSix)
groups7 = counter7 / 4
groups6 = counter6 / 4
while groups7 > 0:
    pd7Groups.append(list())
    groups7 = groups7 - 1
while groups6 > 0:
    pd6Groups.append(list())
    groups6 = groups6 - 1
for aName in pdSeven:
    number = randrange(0, groups7 - 1, 1)
    while len(pd7Groups[number]) > 4:
           number = randrange(0, groups7 - 1, 1)
    pd7Groups[number].append(aName)
for aName in pdSix:
    number = randrange(0, groups6 - 1, 1)
    while len(pd6Groups[number]) > 4:
           number = randrange(0, groups7 - 1, 1)
    pd7Groups[number].append(aName)
print pd7Groups
print pd6Groups

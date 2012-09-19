import random
import math 
pdSix = list()
pdSeven = list()
pd7Groups = list()
pd6Groups = list()

for line in open('ml7-student-names', 'r').readlines():
    name = line.strip().split(",")
    if name[2] == "7":
       #print name;
       pdSeven.append(name)
    else:
        pdSix.append(name)
        #print name;
counter7 = len(pdSeven)
#print counter7
counter6 = len(pdSix)
#print counter6
groups7 = counter7 / 4
g7 = groups7
#print groups7
groups6 = counter6 / 4
g6 = groups6
#print groups6
while (groups7 > 0):
    pd7Groups.append(list())
    groups7 = groups7 - 1
    #print groups7
#print "OUT"
while (groups6 > 0):
    pd6Groups.append(list())
    groups6 = groups6 - 1
    #print groups6
#print "OUT2"
for aName in pdSeven:
    number = random.randrange(0, (g7 - 1), 1)
    print number
    while len(pd7Groups[number]) > 4:
           number = random.randrange(0, (g7 - 1), 1)
           print number
    pd7Groups[number].append(aName)
for aName in pdSix:
    number = random.randrange(0, (g6 - 1), 1)
    print number
    while len(pd6Groups[number]) > 4:
           number = random.randrange(0, (g6 - 1), 1)
           print number
    pd6Groups[number].append(aName)
print "Period 7 Groups:"
for aList in pd7Groups:
   print aList
print "Period 6 Groups:"
for aList in pd6Groups:
   print aList

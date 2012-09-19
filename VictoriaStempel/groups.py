import random

Pd6 = []
Pd7 = []
allnames = []

temp = open("ml7-student-names", "r")

for line in temp:
    line = line.strip()
    allnames.append(line)

for string in allnames:
    if '6' in string:
        Pd6.append(string)
    else:
        Pd7.append(string)

random.shuffle(Pd6)
random.shuffle(Pd7)

def printGroups(l):
    for string in l:
        print string
        if ((l.index(string)+1) % 4) == 0:
             print "\n"

print "6th Period Groups:"
printGroups(Pd6)
print "7th Period Groups:"
printGroups(Pd7)


    



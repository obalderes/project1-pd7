import random

Pd6 = list()
Pd7 = list()
allnames = list()

for line in open("ml7-student-names", "r").readlines():
    allnames.append(line)

for string in allnames:
    if string[-1] == '6':
        string = string[:-2]
        Pd6.append(string)
    elif string[-1] == '7':
        string = string[:-2]
        Pd7.append(string)

Pd6 = random.shuffle(Pd6)
Pd7 = random.shuffle(Pd7)

Pd6counter = 36
Pd7counter = 32

print "Pd 6 Groups:"
while Pd6counter > 0:
    print Pd6(Pd6counter)
    Pd6counter-= 1
    if Pd6counter % 4 == 0:
        print ""
print "Pd 7 Groups:"
while Pd7counter > 0:
    print Pd7(Pd7counter)
    Pd7counter-= 1
    if Pd7counter % 4 == 0:
        print ""

raw_input("Press<enter>")

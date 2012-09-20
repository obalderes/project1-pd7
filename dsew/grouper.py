import random

period6 = []
period7 = []

for line in open("ml7-student-names", "r").readlines():
    if line.find("7") == -1:
        period6.append(line.strip()[:-2])
    else:
        period7.append(line.strip()[:-2])

random.shuffle(period6)
random.shuffle(period7)

print "PERIOD SIX"

for i in range(len(period6)):
    if i % 4 == 0:
        print "\nGroup " + str(i / 4 + 1)
    print period6[i]

print "\nPERIOD SEVEN"

for i in range(len(period7)):
    if i % 4 == 0:
        print "\nGroup " + str(i / 4 + 1)
    print period7[i]

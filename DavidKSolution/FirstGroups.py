#David Kurkovskiy
#Software Development
#Period 7
a = []

for line in open("ml7-student-names", "r").readlines():
    a.append(line)

#print a

six = []
seven = []

for string in a:
    for char in string:
        if char == '6':
            six.append(string)
        elif char == '7':
            seven.append(string)

#print six
#print seven

import random

x = len(six)
y = len(seven)

finalsix = []
finalseven = []

while x > 0:
    randx = random.randrange(0,x)
    q = six[randx]
    six.__delitem__(randx)
    finalsix.append(q)
    x = x - 1

while y > 0:
    randy = random.randrange(0,y)
    r = seven[randy]
    seven.__delitem__(randy)
    finalseven.append(r)
    y = y - 1

#print finalsix
#print finalseven

#print len(finalsix)
#print len(finalseven)

"""For some strange reason, the period six list has 36 names, so I guess there are a lot of doubles. Not my period anyway, so I'll just dole out groups
for period 7! DK 12:54 am 9/13/12"""

#hold = 4
#groupnum = 1

#for string in finalseven:
#    print "Group " + groupnum + ":"
    

hold = 0
groupnum = 1

while hold < len(finalseven):
    print("Group " + str(groupnum) + ": " + str(finalseven[hold:hold+4]))
    hold = hold + 4
    groupnum = groupnum + 1

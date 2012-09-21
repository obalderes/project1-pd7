#the final thing

import random

pd6 = []
pd7 = []
pd6people = 36
pd7people = 32
peoplelist = open("../ml7-student-names", "r").readlines()
a = 0
b = 4
x = 0
y = 4
w = 0 #max 8
z = 0 #max 9

for n in peoplelist:
    if n.find('6') > 0:
        pd6.append(n)

for n in peoplelist:
    if n.find('7') > 0:
        pd7.append(n)

random.shuffle(pd6)
random.shuffle(pd7)


while (w < 8):
    print "Pd 6 Group:" + str(pd6[a:b])
    a = a + 4
    b = b + 4
    w = w + 1

while (z < 9):
    print "Pd 7 Group:" + str(pd7[x:y])
    x = x + 4
    y = y + 4
    z = z + 1


    
        

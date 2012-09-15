from random import shuffle

pd6 = []
pd7 = []
counter = 0
counter2 = 0

for line in open("ml7-student-names").readlines():
    line = line.strip()
    a,b,c = line.split(",")
    if c is '6':
        pd6.append(b+a+c)
    else:
        pd7.append(b+a+c)


#print pd6
#shuffle(pd6)
#print ""
#print pd6

#print ""
#print pd7
#shuffle(pd7)
#print ""
#print pd7

counter = 0
for name in pd6:
    if counter <= 3:
        print name
        counter+= 1
    else:
        print 
        print name
        counter = 1

print    

counter = 0
for name in pd7:
    if counter <= 3:
        print name
        counter+= 1
    else:
        print
        print name
        counter = 1

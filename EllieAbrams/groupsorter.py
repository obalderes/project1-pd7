from random import shuffle

pd6 = []
pd7 = []

for line in open ("ml7-student-names").readlines():
    line = line.strip()
    lname, fname, pd = line.split(",")
    if pd is "6":
        pd6.append(fname+" "+lname)
    else:
        pd7.append(fname+" "+lname)

shuffle(pd6)
shuffle(pd7)

print "Period Six Groups:"
print
counter = 0
for student in pd6:
    if counter <=3:
        print student
        counter+= 1
    else:
        print
        print student
        counter = 1

print
print "Period Seven Groups:"
print
counter = 0
for student in pd7:
    if counter <=3:
        print student
        counter+= 1
    else:
        print
        print student
        counter = 1

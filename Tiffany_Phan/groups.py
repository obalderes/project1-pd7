#Tiffany Phan Pd. 7

import random

pd6 = []
pd7 = []
masterlist = []

for line in open("ml7-student-names", "r").readlines():
    masterlist.append(line)

for student in masterlist: 
    for period in student:
        if period == '6':
            pd6.append(student.strip())
        if period == '7': 
            pd7.append(student.strip())

#Method to make the groups of 4 within each period
def makeGroups(period):
    numOfGroup = 1
    temp = 0
    s = "\nGroup "
    s2 ="%s%d"%(s,numOfGroup)
    for student in period:
        print student
        temp = temp + 1
        if temp % 4 == 0:
            numOfGroup = numOfGroup + 1
            print s2
        

#Shuffle students within each period
random.shuffle(pd6)
random.shuffle(pd7)

#Make and print out groups
print "GROUPS FOR PERIOD 6\n"
makeGroups(pd6)
print "GROUPS FOR PERIOD 7\n"
makeGroups(pd7)


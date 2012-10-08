#GRUPO UNO
#this is what creates the personal info and group databases/shelves
#I don't think this needs to be run very often, so please don't

import shelve

students = open('students.txt')
sList = students.readlines()
students.close()

Pd6 = shelve.open('GroupInfoPd6.dat')
Pd7 = shelve.open('GroupInfoPd7.dat')
i = 0
while i<8:
    Pd6[str(i)]=list()
    Pd7[str(i)]=list()
    i+=1
info = shelve.open('PersonalInfo.dat')
for line in sList:
    email = line[ : line.find(',')]
    line = line[line.find(',',1) : ]
    last = line[1 : line.find(',',1)]
    line = line[line.find(',',1) : ]
    first = line[1 : line.find(',',1)]
    line = line[line.find(',',1) : ]
    ID = line[1 : line.find(',',1)]
    line = line[line.find(',',7) : ]
    period = line[1:line.find(',',1)]
    group=line[-2]
    #period 0 is 6th period, 1 is 7th
    info[email] = [ last, first, ID, period, group]
    if period>'0':
        temp=Pd7[group]
        temp.append(email)
        Pd7[group]=temp
    else:
        temp=Pd6[group]
        temp.append(email)
        Pd6[group]=temp
print Pd6
print Pd7

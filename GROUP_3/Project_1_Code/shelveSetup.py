#!/usr/bin/python 

import shelve

a = shelve.open("students")


file1 = open("students.txt")

for line in file1:
    line = line.strip()
    line = line.split(",")
    email = line.pop(0)
    a[email] = line

a.close()
file1.close()

b = shelve.open("groups")

file2 = open("p1.txt")

for line in file2:
    line = line.strip()
    line = line.split(",")
    groupNumber = line.pop(0)
    b[groupNumber] = line
    
 
b.close()
file2.close()

c = shelve.open("grades")

file3 = open("students.txt")

for line in file3:
    line = line.strip()
    line = line.split(",")
    email = line.pop(0)
    c[email] = [[],[],[],[]]
    for location in range(1,4):
        c[email].append([5])


c.close()
file3.close()

d = shelve.open("ratedBy")

file4 = open("students.txt")

for line in file4:
    line = line.strip()
    line = line.split(",")
    email = line.pop(0)
    d[email] = []

d.close()
file4.close()


e = shelve.open("nameToGroupNumber")

file5 = open("p1.txt")

for line in file5:
    line = line.strip()
    line = line.split(",")
    
    e[line[1]] = line[0]
    e[line[2]] = line[0]
    e[line[3]] = line[0]
    if len(line) > 4:
        e[line[4]] = line[0]

e.close()
file5.close()

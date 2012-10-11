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
    c[email] = [4] []

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

#!/usr/bin/python 

import shelve


def getStudentInfo():
    a = shelve.open("students", writeback=True)


    file1 = open("students.txt")

    for line in file1:
        line = line.strip()
        line = line.split(",")
        email = line.pop(0)
        a[email] = line

    a.close()
    file1.close()


def getGroups():
    b = shelve.open("groups", writeback=True)

    file2 = open("p1.txt")

    for line in file2:
        line = line.strip()
        line = line.split(",")
        email = line.pop(0)
        b[email] = line
 
    b.close()
    file2.close()


def setupGrades():
    c = shelve.open("grades", writeback=True)

    file3 = open("students.txt")

    for line in file3:
        line = line.strip()
        line = line.split(",")
        email = line.pop(0)
        c[email] = []

    c.close()
    file3.close()


def setupRatedBy():
    d = shelve.open("ratedBy", writeback=True)

    file4 = open("students.txt")

    for line in file4:
        line = line.strip()
        line = line.split(",")
        email = line.pop(0)
        d[email] = []

    d.close()
    file4.close()


    
    



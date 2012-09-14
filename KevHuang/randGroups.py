#!/bin/python
import random

a1 = []
a2 = []
myFile = open("ml7-student-names")
for i in myFile.readlines():
    i= i.strip()
    if i.split(",")[2] == "6":
        a1.append(i.split(",")[1] +" "+ i.split(",")[0])
    else:
        a2.append(i.split(",")[1] +" "+ i.split(",")[0])
myFile.close()

def randomGroup(x):
    for i in range(1000):
        b = random.randrange(len(a1)-1)
        c = random.randrange(len(a1)-1)
        a1[b],a1[c] = a1[c],a1[b]
    for i in range(1000):
        b = random.randrange(len(a2)-1)
        c = random.randrange(len(a2)-1)
        a2[b],a2[c] = a2[c],a2[b]   
    tmp=0
    print "These are period 6 groups: \n"
    for i in range(len(a1)):
        print a1[i]
        if tmp % x == 3 :
            print ""
        tmp=tmp+1
    print "These are period 7 groups: \n"
    for i in range(len(a2)):
        print a2[i]
        if tmp % x == 3 :
            print ""
        tmp=tmp+1

randomGroup(4)

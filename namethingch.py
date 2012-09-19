#!/usr/bin/python


from random import shuffle

period6=[]
period7=[]

f=open("ml7-student-names")

for i in f.readlines():
    line=i.strip()
    last,first,period=line.split(",")
    if period=="6":
        period6.append(first+" "+last+" ,"+period)
    else:
        period7.append(first+" "+last+" ,"+period)

shuffle(period6)
shuffle(period7)

people=0

print "Period 6 Groups"

for student in period6:
    print student
    people += 1
    if people == 4:
        print "\n"
        people=0

print "Period 7 Groups"

for student in period7:
    print student
    people += 1
    if people == 4:
        print "\n"
        people=0

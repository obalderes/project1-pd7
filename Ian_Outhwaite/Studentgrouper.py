#Pros: only uses one list!
#Cons: Has a run time of O(3n), where n is the number of students

from random import shuffle
count=0
kids = []

#Creates a list with names in the format 'first last, period'
for line in open("ml7-student-names").readlines():
    clean = line.strip()
    last,first,p = clean.split(",")
    kids.append(first+" "+last+", "+p)

#shuffles the list
shuffle(kids)

#prints out the groups for period 6
for person in kids:
    kid,p = person.split(", ")
    if p is '6':
        print person
        count += 1
        if count%4 == 0:
            print

print
count=0

#prints out the groups for period 7
for person in kids:
    kid,p = person.split(", ")
    if p is '7':
        print person
        count += 1
        if count%4 == 0:
            print

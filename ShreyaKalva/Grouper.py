#Shreya Kalva, Software Development Period 7

import random

#Creating the Period 6 and Period 7 lists:

per6 = []
per7 = []

#Opening the student names text file, reading the names into a list,
#and sorting those names even further into two lists based on their periods (the
#names are sorted and stored as "first, last" for each period):

for line in open("ml7-student-names.txt","r").readlines():
    newLine = line.strip()
    lastName,firstName,periodNumber = newLine.split(",")
    if (periodNumber == "6"):
        per6.append(firstName + " " + lastName)
    else:
        per7.append(firstName + " " + lastName)

#Randomly shuffling the names in each period's list:

random.shuffle(per6)
random.shuffle(per7)

#Dividing the names in Period 6's list into groups of four:

counter1 = 1
if counter1 == 1:
    print "Period 6 Groups"
    print
for person in per6:
    print person
    if counter1 % 4 == 0:
        print
    counter1 += 1

#Dividing the names in Period 7's list into groups of four:
    
counter2 = 1
if counter2 == 1:
    print
    print
    print
    print "Period 7 Groups"
    print
for person in per7:
    print person
    if counter2 % 4 == 0:
        print 
    counter2 += 1



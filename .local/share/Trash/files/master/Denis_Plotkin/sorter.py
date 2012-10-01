#!/usr/bin/python

from random import random


sixthPeriod = []
seventhPeriod = []

lines = [line.strip() for line in open("ml7-student-names")]
usedIndices = [-1]
counter = 0
randomizer = -1

while counter < len(lines):
    while randomizer in usedIndices:
        randomizer = int(random() * len(lines)) 
    usedIndices.append(randomizer)
    line = lines[randomizer]
    lastName,firstName,period = line.split(",")
    if period == "6":
        fullName = firstName + " " + lastName
        sixthPeriod.append(fullName)
    else:
        fullName = firstName + " " + lastName
        seventhPeriod.append(fullName)
    counter = counter + 1


while len(sixthPeriod) % 4 != 0:
    sixthPeriod.append(":)")

while len(seventhPeriod) % 4 != 0:
    seventhPeriod.append(":)")

print
print "6th Period Groups:"
sixthPeriodCounter = 0
sixthPeriodGroupCounter = 1
while sixthPeriodCounter < len(sixthPeriod):
    print "Group " + str(sixthPeriodGroupCounter) + ":\t" + sixthPeriod[sixthPeriodCounter] + ", " + sixthPeriod[sixthPeriodCounter + 1]  + ", " + sixthPeriod[sixthPeriodCounter + 2]  + ", " + sixthPeriod[sixthPeriodCounter + 3]
    sixthPeriodCounter = sixthPeriodCounter + 4
    sixthPeriodGroupCounter = sixthPeriodGroupCounter + 1
  
print
print "7th Period Groups:"
seventhPeriodCounter = 0
seventhPeriodGroupCounter = 1
while seventhPeriodCounter < len(seventhPeriod):
    print "Group " + str(seventhPeriodGroupCounter) + ":\t" + seventhPeriod[seventhPeriodCounter] + ", " + seventhPeriod[seventhPeriodCounter + 1]  + ", " + seventhPeriod[seventhPeriodCounter + 2]  + ", " + seventhPeriod[seventhPeriodCounter + 3]
    seventhPeriodCounter = seventhPeriodCounter + 4
    seventhPeriodGroupCounter = seventhPeriodGroupCounter + 1

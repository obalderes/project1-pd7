# Izzi Clark

from random import shuffle  #see below for an explanation

# makes a list for each period
pd6 = []
pd7 = []

# reads and preps each line in the doc
for line in open("ml7-student-names").readlines():
    line = line.strip()                     # separates components of each line
    last,first,pd = line.split(",")         # gets rid of commas
    if pd is "6":                           # divides names into two lists based on period
        pd6.append(first+" "+last)
    if pd is "7":
        pd7.append(first+" "+last)

#shuffles the names in each list - who woulda thunk?
shuffle(pd6)
shuffle(pd7)

#prints groups for pd6, then does the same for pd7
print "**PERIOD 6**"
print
counter = 0
for student in pd6:
    print student
    counter+= 1
    if counter is 4:
        print          # prints empty line to separate groups of 4
        counter = 0    # and resets counter to 0
print
print "**PERIOD 7**"
print
counter = 0
for student in pd7:
    print student
    counter+= 1
    if counter is 4:
        print
        counter = 0

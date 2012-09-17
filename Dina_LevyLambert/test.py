#!/user/bin/python

import random

#period lists
p6 = []
p7 = []

#reformat line and divide the list of names into their periods

for line in open("ml7-student-names", "r").readlines():
    newLine = line.strip()
    goodLine = newLine.split(',')
    betterLine = goodLine[1] + " " + goodLine[0]
    if goodLine[2] == "7":
        p7.append(betterLine)
    else:
        p6.append(betterLine)

#randomize order in both periods
random.shuffle(p6)
random.shuffle(p7)


#makes lists for the periods and counter
listPeriods = [p6, p7]
counter = 1

#distributes into groups
for name in listPeriods:
    print "\n"
    if counter == 1 :
        print "PERIOD 6 GROUPS"
        counter+= 1
    else :
        print "PERIOD 7 GROUPS"
    for num in range(1, len(name) / 4 + 1): #iterate as many times as there are groups
        print "\n\tGROUP " + str(num) + ":"  #print group number
        for num in range(0, 4):
            if not name: #if no name is left the loop breaks
                print "\n"
                break
            else:
                print "\t" + str(name.pop(0)) #prints next name



                            

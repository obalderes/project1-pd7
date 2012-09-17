#!/user/bin/python

import random
groupNumber = 4

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






                            

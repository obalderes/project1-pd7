import random

#Period Lists
per6 = []
per7 = []

#Seperate based on Period
for line in open("ml7-student-names","r").readlines();
    line = line.strip();
    f,l,p = line.split(,);
    if p == 6
        per6.append(f+" "+l);
    else
        per7.append(f+" "+l);

#Randomize Period 6
random.shuffle(per6);

#Randomize Period 7
random.shuffle(per7);

#Print out Period 6
counter = 0
numGroups = 1
while numGroups < 10
     print "Group " + numGroups + " "
    x = 0
    while x < 4
        print per6[counter]
        x = x + 1
        counter = counter + 1
    numGroups = numGroups - 1

#Print out Period 7
counter2 = 0
numGroups2 = 1
while numGroups2 < 9
    print "Group " + numGroups2 + " "
    y = 0
    while y < 4
        print per7[counter2]
        y = y + 1
        counter2 = counter2 + 1
    numGroups2 = numGroups2 - 1
        
        



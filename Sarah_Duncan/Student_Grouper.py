#!/usr/bin/python

import ml7-student-names

names_list = []
names_list_6 = []
randomized_groups_6 = []
names_list_7 = []
randomized_groups_7 = []
size = 0
size6 = 0
size7 = 0
counter = 1
counter6 = 1
counter7 = 1

def makeClassLists():
    for line in ml7-student-names:
        names_list.append(line)
        size++
    names_list.append("\n")
    s = ""
    while(counter <= size):
        s = names_list.pop(0)
        if(s.endswith("6")):
            names_list_6.append(s)
            size6++
        else:
            names_list_7.append(s)
            size7++
        counter = counter + 1

    
def randomizeLists():
    random.shuffle(names_list_6)
    random.shuffle(names_list_7)

def formGroups():
    while (counter6 <= size6):
        if((counter6 - 1) % 4 == 0):
            randomized_groups_6.append("Group %d", (counter - 1) / 4)
        randomized_groups_6.append(names_list_6.pop(0))
        if(counter6 % 4 == 0):
            randomized_groups_6.append("\n -------------------------- \n")
        counter6 = counter6 + 1
    while(counter7 <= size7):
        if((counter7 - 1) % 4 == 0):
            randomized_groups_7.append("Group %d", (counter - 1) / 4)
        randomized_groups_7.append(names_list_7.pop(0))
        if(counter7 % 4 == 0):
            randomized_groups_7.append("\n -------------------------- \n")
        counter7 = counter7 + 1

def printGroups():
    

#!/usr/bin/python
import os
import random

file = open(os.path.join(os.pardir,'ml7-student-names'), 'r')
names_list = []
names_list_6 = []
randomized_groups_6 = ""
names_list_7 = []
randomized_groups_7 = ""
size = 0
size6 = 0
size7 = 0
counter = 1
counter6 = 1
counter7 = 1

def makeClassLists():
    for line in file:
        names_list.append(line)
        size = size + 1
    names_list.append("\n")
    s = ""
    while(counter <= size):
        s = names_list.pop(0)
        if(s.endswith("6")):
            names_list_6.append(s)
            size6 = size6 + 1
        else:
            names_list_7.append(s)
            size7 = size7 + 1
        counter = counter + 1

    
def randomizeLists():
    random.shuffle(names_list_6)
    random.shuffle(names_list_7)

def formGroups():
    while (counter6 <= size6):
        if((counter6 - 1) % 4 == 0):
            randomized_groups_6 += ("Group %d", (counter - 1) / 4)
        randomized_groups_6 += names_list_6.pop(0)
        if(counter6 % 4 == 0):
            randomized_groups_6 += "-------------------------- \n"
        counter6 = counter6 + 1
    while(counter7 <= size7):
        if((counter7 - 1) % 4 == 0):
            randomized_groups_7 += ("Group %d", (counter - 1) / 4)
        randomized_groups_7 += names_list_7.pop(0)
        if(counter7 % 4 == 0):
            randomized_groups_7 += "-------------------------- \n"
        counter7 = counter7 + 1

def main():
    makeClassLists()
    randomizeLists()
    formGroups()

print("6th Period: \n" + randomized_groups_6 + "\n")
print("7th Period: \n" + randomized_groups_7 + "\n")

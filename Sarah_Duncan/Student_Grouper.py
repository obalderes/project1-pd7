#!/usr/bin/python
import os
import random

file = open(os.path.join(os.pardir,'ml7-student-names'), 'r')


def makeClassLists():
    global names_list
    global names_list_6
    global names_list_7
    global size6
    global size7
    names_list =  file.readlines()
    names_list_6 = []
    names_list_7 = []
    size6 = 0
    size7 = 0
    for item in names_list:
        if('6' in item):
            names_list_6.append(item)
            size6 = size6 + 1
        else:
            names_list_7.append(item)
            size7 = size7 + 1
    
def randomizeLists():
    random.shuffle(names_list_6)
    random.shuffle(names_list_7)

def formGroups():
    global randomized_groups_6
    global randomized_groups_7
    randomized_groups_6 = ''
    randomized_groups_7 = ''
    counter = 1
    counter6 = 1
    counter7 = 1
    while (counter6 <= size6):
        if((counter6 - 1) % 4 == 0):
            randomized_groups_6 += ("Group #" + str(((counter - 1) / 4) + 1) + "\n")
        randomized_groups_6 += names_list_6.pop(0)
        if(counter6 % 4 == 0):
            randomized_groups_6 += "-------------------------- \n"
        counter6 = counter6 + 1
        counter = counter + 1
    while(counter7 <= size7):
        if((counter7 - 1) % 4 == 0):
            randomized_groups_7 += ("Group #" + str(((counter - 1) / 4) + 1) + "\n")
        randomized_groups_7 += names_list_7.pop(0)
        if(counter7 % 4 == 0):
            randomized_groups_7 += "-------------------------- \n"
        counter7 = counter7 + 1
        counter = counter + 1


makeClassLists()
randomizeLists()
formGroups()

print("6th Period: \n" + randomized_groups_6 + "\n")
print("7th Period: \n" + randomized_groups_7 + "\n")

file.close()

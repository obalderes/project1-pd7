#Leopold Spohngellert
#Mr. Zamansky Period 7
#Project 1 


#!/usr/bin/python
import random

file = open("ml7-student-names", "r+");
st = file.readlines()

l =  len(st)
#print st[random.randint(0,l-1)]



def classList():
    i = 0
    b = 1
    currentPeriod = 0
    whichP = 0
    while i < l:
        z = random.randint(0, l-1)
        if (st[z].find("7") == -1):
            whichP = 6
        else:
            whichP = 7
       
        if st[z] != "empty":
            if (i % 4 == 0):
                currentPeriod = whichP
                print "Group" + " " + repr(b) + " consists of:\n"
                b = b + 1
                
            if (currentPeriod == whichP):
                print st[z]
                st[z] = "empty"
                i = i + 1
           

print "\nThe following are randomized groups of four:\n \n"
classList() 


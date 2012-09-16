#Leopold Spohngellert
#Mr. Zamansky Period 7
#Project 1 


#!/usr/bin/python
import random

file = open("ml7-student-names", "r+");
st = file.readlines()

l =  len(st)
print l
#print st[random.randint(0,l-1)]


def classList():
    i = 0
    b = 1
    while i < 68:
        z = random.randint(0, l-1)
        if st[z] != "empty":
            if (i % 4 == 0):
                print "Group" + " " + repr(b) + " consists of:\n"
                b = b + 1
            print st[z]
            st[z] = "empty"
            i = i + 1
           


classList()


        
        
        
    


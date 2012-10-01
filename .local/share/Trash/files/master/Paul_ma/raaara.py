import random

#lists for pd6&7
list6 = list()
list7 = list()

#Sort txt file into pd lists
for text in open("ml7-student-names", "r").readlines():
    text = text.strip()
    last,first,period = text.split(",")
    if (period == "6"):
        list6.append(first+ " " + last)
    else:
        list7.append(first+ " "+ last)


print "Pd 6"
random.shuffle(list6)
for element in range(len(list6)):
    if(element%4 ==0):
        print " "
    print list6[element]
    
print "\n + \n"

print "Pd 7"
random.shuffle(list7)
for element in range(len(list7)):
    if(element%4 ==0):
        print " "
    print list7[element]

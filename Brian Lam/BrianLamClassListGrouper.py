import random

#Create lists for period 6 and 7
list6 = list()
list7 = list()

#Sort the text file into lists based on period
for text in open("ml7-student-names", "r").readlines():
    text = text.strip()
    last,first,period = text.split(",")
    if (period == "6"):
        list6.append(first+ " " + last)
    else:
        list7.append(first+ " "+ last)

#shuffle lists and print them out in groups of four people
print "Period 6"
random.shuffle(list6)
for element in range(len(list6)):
    if(element%4 ==0):
        print " "
    print list6[element]
    
print " "+"\n"+"---------"+"\n"+" "

print "Period 7"
random.shuffle(list7)
for element in range(len(list7)):
    if(element%4 ==0):
        print " "
    print list7[element]

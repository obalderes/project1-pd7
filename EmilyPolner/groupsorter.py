import random

pd6 = list()
pd7 = list()
listofallnames = list()

for line in open("ml7-student-names", "r").readlines():
    listofallnames.append(line)

for string in listofallnames:
    for char in string:
        if char == '6':
            pd6.append(string)
        elif char == '7':
            pd7.append(string)

def shuffle6():
    for people in pd6:
        print people
        Groupnum = 1
        if(pd6.index(people)) % 4 == 2:
            print "\n Group" 
                print Groupnum
        Groupnum++

def shuffle7():
   for people in pd7:
        print people
        Groupnum2 = 1
        if(pd7.index(people)) % 4 == 2:
            print "\n Group" 
                print Groupnum2
        Groupnum2++

def groupmaker(list):
    random.shuffle(list)
    if list == pd6:
        shuffle6()
    if list == pd7:
        shuffle7()

print "Groups in 6th pd:"
groupmaker(pd6)

print "\n Groups in 7th pd:"
groupmaker(pd7)

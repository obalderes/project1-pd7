import random
L = []
names6 = []
names7 = []

def reader(data):
    """
    reads the file into a list
    """
    return open(data).readlines()

L = reader("ml7-student-names")
n = len(L)

#this sorts the items into their individual periods
for item in L:
    item = item.strip()
    if (item[-1] == "7"):
        names7.append(item)
    elif item[-1]=="6":
        names6.append(item)
    else:
        print "ZZZ",item

def randomizer(period):
    """
    shuffles the items in the list and gives each person a group number
    """
    a = []
    random.shuffle(period)
    group = 0
    num = -1
    for item in period:
        if num < 3:
            item = item + ", "
            a.append("%s%d"%(item,group))
            num = num + 1
        else:
            group = group + 1
            num = 0
            item = item + ", "
            a.append("%s%d"%(item,group))
    return a
        


 

names6 = randomizer(names6)
names7 = randomizer(names7)

print len(names6)
print len(names7)

print "Period 6 Groups"
print "last, first, period, group #"
for item in names6:
    print item
print
print "Period 7 Groups"
print "last, first, period, group #"
for item in names7:
    print item

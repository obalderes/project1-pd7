import random

nameList = open("ml7-student-names.txt").readlines()
list6 = []
list7 = []

for line in nameList:
    line = line.strip()
    if (line[-1] == "6"):
        list6.append(line)
    elif line[-1] == "7":
        list7.append(line)
    else:
        print line

def randomize (pdList, gpsize):
    random.shuffle(pdList)
    finalList = []
    grp = 0
    i = -1
    for line in pdList:
        if i < gpsize - 1:
            line = line + ", "
            finalList.append("%s%d"%(line,grp))
            i += 1
        else:
            grp += 1
            i = 0
            line = line + ", "
            finalList.append("%s%d"%(line,grp))
    return finalList

list6 = randomize(list6, 4)
list7 = randomize(list7, 4)
print "Pd 6"
for line in list6:
    print line
print
print "Pd 7"
for line in list7:
    print line

            



        

#!/user/bin/python

from random import randrange
groupSize = 4

#creates a list of names for each period
pd6 = []
pd7 = []
for line in open("names", "r").readlines():
    #formats line to firstName_space_lastName
    strippedLine = line.strip()
    splitLine = strippedLine.split(',')
    fullName = splitLine[1] + " " + splitLine[0]
    #separates names into period 6 and 7
    if splitLine[2] == "6":
        pd6.append(fullName)
    else:
        pd7.append(fullName)


#generates random groups for each period
pds = [pd6, pd7]
pdHeadings = ["PD 6 GROUPS", "PD 7 GROUPS"]

for pd in pds:
    print "\n" + pdHeadings.pop(0)
    for i in range (1, len(pd) / groupSize + 1):
        print "\tGroup " + str(i) + ":"
        #while period isn't empty, prints members of current group
        for i in range (0, groupSize):
            if not pd:
                break
            else:
                print "\t\t" + str(pd.pop(randrange(0, len(pd))))

#!/user/bin/python

from random import randrange
groupSize = 4


#puts lines from ml7-student-names file in 'lines'
f = open("names", "r")
lines = f.readlines()

#puts names in either 'pd6' or 'pd7'
pd6 = []
pd7 = []
for line in lines:
    #sets pd to the only digit in the line, either 6 or 7
    pd = filter(str.isdigit, line)
    if pd == "6":
        #transforms line to firstName_space_lastName and adds to pd6
        strippedLine = line.strip()
        splitLine = strippedLine.split(',')
        fullName = splitLine[1] + " " + splitLine[0]
        pd6.append(fullName)
    else:
        #transforms line to firstName_space_lastName and adds to pd7
        strippedLine = line.strip()
        splitLine = strippedLine.split(',')
        fullName = splitLine[1] + " " + splitLine[0]
        pd7.append(fullName)

print "\n"

#generates and prints random groups for period 6
print "PD 6 GROUPS:"
for i in range (1, len(pd6) / groupSize + 1):
    print "\tGroup " + str(i) + ":"
    #while pd6 isn't empty, lists out the members of current group
    for i in range (0, groupSize):
        if not pd6:
            break
        else:
            print "\t\t" + str(pd6.pop(randrange(0, len(pd6))))

print "\n"

#generates and prints random groups for period 7
print "PD 7 GROUPS:"
for i in range (1, len(pd7) / groupSize + 1):
    print "\tGroup " + str(i) + ":"
    #while pd7 isn't empty, lists out the members of current group   
    for i in range (0, groupSize):
        if not pd7:
            break
        else:
            print "\t\t" + str(pd7.pop(randrange(0, len(pd7))))

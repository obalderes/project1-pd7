#This is Bernie's group picker project

import random

f = open('ml7-student-names','r')
pd6 = []
pd7 = []
groups = []

def main():
   #printLines()
    splitLinesIntoClasses()
   #print "pd6: " + str(pd6)
   #print "pd7: " + str(pd7)
    classesToGroups(pd6)
    classesToGroups(pd7)
   #print groups
    printGroups()
 #print "is this tabbing?"
 

#names = file.read()
#print names
def printLines():
    print "in printLines"
    #f = open('ml7-student-names','r')
    namelines = f.readlines()
    n = 0
    for line in namelines:
        print str(n) + ": " + line
        n = n + 1
    print "end of printLines"

def splitLinesIntoClasses():
    #f = open('ml7-student-names','r')
    nameLines = f.readlines()
    #n = 0
    for line in nameLines:
       #print str(n) + ": " + str(line.split(','))
       #n = n + 1
        l = line.split(',')
        if '6\n' in l:
            pd6.append(l)
        else:
            pd7.append(l)
    print "end of splitLines"
#print file.readline()
    
def classesToGroups(l):
    classList = l
    for i in classList:
        tempGroup = []
        for n in range(4):
            p = random.randrange(0,len(classList))
            tempGroup.append(classList[p])
            classList.remove(classList[p])
        groups.append(tempGroup)

def lineToString(l):
    string = ""
    string = l[1] + " " + l[0] + ", Period " + str(l[2])
    return string

def printGroups():
    n = 0
    for i in groups:
        string = "Group " + str(n+1) + ":\n"
        num = 0
        for l in groups[n]:
            string = string + lineToString(groups[n][num])
            num = num + 1
        print string
        n = n+1

main()

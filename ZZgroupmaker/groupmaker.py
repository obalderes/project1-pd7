def loadnames(path):
    """
    loadnames(path)
    
    Loads the names from the given file into a namelist and returns that list.
    The namelist contains an entry for every person.
    Each person's entry is a list with three entries: Lastname, Firstname, Period
    
    The format of the text file should be one line for each entry:
    Lastname,Firstname,Period

    Returns a namelist: [ [last,first,pd],...,[smith,john,7] ]
    """
    namelist = open(path, mode="r").readlines()
    namelist[:] = [line.strip().split(",") for line in namelist]
    return namelist

def splitperiods(namelist,x,y):
    """
    splitperiods(namelist,x,y)
    
    Returns a periodlist with two entries, one for each period, x and y.
    The entry for each period is a namelist with an entry for each person in that period.
    Each person's entry is a list with three entries: Lastname, Firstname, Period

    Returns a periodlist: [ [namelist for period x],[namelist for period y] ]
    """
    periodlist = [[],[]]
    for person in namelist:
        if int(person[2]) == x:
            periodlist[0].append(person)
        elif int(person[2]) == y:
            periodlist[1].append(person)
        else:
            print "error: not in one of the given periods, in period" + person[2]
    return periodlist

def makegroups(periodlist,groupsize):
    """
    magegroups(periodlist,groupsize)
    
    Takes in a scrambled periodlist and returns a grouplist.
    Each entry in the grouplist is for a different period.
    Each period has an entry for every group.
    The list for the group contains 'groupsize' entries, one for each person in the group.
    Each person's entry is a list with three entries: Lastname, Firstname, Period

    Returns a grouplist: [ [[g1 in p6],...,[g8 in p6]], [[g1 in p7],...,[g8 in p7]] ]
    """
    grouplist = [[],[]]
    for x in xrange(len(periodlist[0])/groupsize):
        group = []
        for y in xrange(groupsize):
            group.append(periodlist[0][x*groupsize+y])
        grouplist[0].append(group)
    for x in xrange(len(periodlist[1])/groupsize):
        group = []
        for y in xrange(groupsize):
            group.append(periodlist[1][x*groupsize+y])
        grouplist[1].append(group)
    return grouplist

def printgroups(grouplist):
    """
    printgroups(grouplist)
    
    Prints a grouplist in an organized fashion.
    """
    print ""
    for period in grouplist:
        print "Period " + period[0][0][2] + ":"
        for group in period:
            s = ""
            for student in group:
                s+= student[1] + " " + student[0] + ", "
            print s[:-2]
        print ""

##########################################################################################

import random
allnames = loadnames("ml7-student-names")
random.shuffle(allnames)
printgroups(makegroups(splitperiods(allnames,6,7),4))


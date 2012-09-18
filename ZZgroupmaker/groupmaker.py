#####################################
#####################################
####                             ####
####      ZACHARY ZIMMERMAN      ####
####    SOFTWARE  DEVELOPMENT    ####
####     SEPTEMBER 15,  2012     ####
####                             ####
#####################################
#####################################

def loadnames(path):
    """
    loadnames(path)
    Makes a list with an entry for each person
    Returns a namelist: [ [last,first,pd],...,[smith,john,7] ]
    """
    # make a list with one entry for each line
    namelist = open(path).readlines()
    # make each line into a list with values for last, first, and pd
    namelist[:] = [line.strip().split(",") for line in namelist]
    return namelist

def splitperiods(namelist,x,y):
    """
    splitperiods(namelist,x,y)
    Makes two namelists, one for each period.
    Returns a periodlist: [ [namelist for period x],[namelist for period y] ]
    """
    periodlist = [[],[]]
    # for each person, check which period they are in
    # and put them in the right list.
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
    makegroups(periodlist,groupsize)
    Split the people up into groups of the given size.
    Returns a grouplist: [ [[g1 in p6],...,[g8 in p6]], [[g1 in p7],...,[g8 in p7]] ]
    """
    grouplist = [[],[]]
    
    # find the number of groups to be made
    for x in xrange(len(periodlist[0])/groupsize):
        group = []
        # put the right number of people in the group
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
# I first split the people by period, then make the groups, and then print it all out.
printgroups(makegroups(splitperiods(allnames,6,7),4))


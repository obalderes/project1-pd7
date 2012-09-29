from flask import Flask

import shelve


def fixNames(data):
    """
    Changes the datafile recieved into a string of first,last,email
    Returns the list of names in the format [first,last,email first,last,email...], etc.
    """
    pass

def createGroups(data):
    """
    Makes the Groups shelve
    """
    groups = shelve.open("groups")
    f = open(data).readlines()
    num = 0
    for item in f:
        a,b = item.split(",",1)
        c = b.split(",")
        #print c
        for item in c:
            groups[item] = c
            print "key then item"
            print item
            print groups[item]
            num = num + 1
    # print f
    print num
    groups.close()

      
    pass

def createQuestions(data):
    """
    Makes the Questions shelve
    """

    pass

createGroups("p1.txt")
f = shelve.open("groups")
print len(f)
print f.keys()

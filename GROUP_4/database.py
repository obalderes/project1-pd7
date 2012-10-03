from flask import Flask

import shelve


def makeAuth(data):
    
    

def fixNames(names,questions):
    """
    Changes the datafile received into a string of first,last,email
    Returns the list of names in the format [first,last,email first,last,email...], etc.
    """
    quest = shelve.open("questions.dat")
    f = open(names).readlines()
    q = open(questions).readlines()
    for item in f:
        item = item.strip()
    for item in q:
        item = item.strip()

    qr = {}
    for item in q:
        qr[item] = []
    
    for item in f:
        a,b = item.split(",",1)
        c = b.split(",")
        for item in c:
            quest[item] = qr

    #for item in quest:
    #    print "/nNEXT ITEM"
    #    print item
    #    print quest[item]

    quest.close()
    pass
    

def createGroups(data):
    """
    Makes the Groups shelve

    Entire group is referenced by the key -- so when we do the list to show who is in the group, just make sure to take out the email that is the key.
    """
    groups = shelve.open("groups")
    f = open(data).readlines()
    for item in f:
        item = item.strip()
    num = 0
    for item in f:
        a,b = item.split(",",1)
        c = b.split(",")
        for item in c:
            groups[item] = c

    groups.close()
    pass



def testing():
    gr = shelve.open("groups")
    print gr.keys()


createGroups("p1.txt")
fixNames("p1.txt","questions.txt")


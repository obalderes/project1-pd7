from flask import Flask

import shelve


def makeAuth():
    """
    Takes students.dat as a parameter, makes a shelve named 'authen'.
    The keys are emails, the items are lists with [first,last,idnum,group].
    Used to authenticate login.
    """
    auth = shelve.open("authen")
    f = open("students.dat").readlines()
    for item in f:
        item = item.strip()
        email,last,first,idnum,cl,sect,pd,group = item.split(",")
        auth[email] = [first,last,idnum,group]
        print email
        print auth[email]

    pass
                
    

def fixNames():
    """
    Changes the datafile received into a string of first,last,email
    Returns the list of names in the format [first,last,email first,last,email...], etc.
    """
    quest = shelve.open("questions.dat")
    f = open("p1.dat").readlines()
    q = open("questions.txt").readlines()
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
    

def createGroups():
    """
    Makes the Groups shelve

    Entire group is referenced by the key -- so when we do the list to show who is in the group, just make sure to take out the email that is the key.
    """
    groups = shelve.open("groups")
    f = open("p1.dat").readlines()
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


#createGroups("p1.txt")
#fixNames("p1.txt","questions.txt")
makeAuth()

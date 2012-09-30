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

def createQuestions(data):
    """
    Makes the Questions shelve
    """

    pass


def testing():
    gr = shelve.open("groups")
    print gr.keys()


#testing()


createGroups("p1.txt")
f = shelve.open("groups")
print len(f)
print f.keys()
f.close()


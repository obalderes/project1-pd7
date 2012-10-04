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
    Takes 'questions.txt' and 'p1.dat'.
    Creates shelve 'questions.dat'
    This shelve has keys as emails.
    The emails refer to a list.
    At each index of the list there is a list of ratings refering to that question.
    """
    quest = shelve.open("questions.dat")
    f = open("p1.txt").readlines()
    q = open("questions.txt").readlines()
    num = len(q)
     
    for item in f:
        item = item.strip()
        a,b = item.split(",",1)
        c = b.split(",")
        for item in c:
            quest[item] = []

    qr = {}
    """
    make the emails refer to a dictionary that will hold emails that refer to a list of ratings (the ratings would refer to the questions in order)
    """

    for item in quest:
        tmp = quest[item]
        while num > 0:
            tmp.append([])
            quest[item] = tmp
            num = num - 1
        if num <= 0:
            num = len(q)
        
    quest.close()
    pass
    

def createGroups():
    """
    Makes the Groups shelve

    Entire group is referenced by the key -- so when we do the list to show who is in the group, just make sure to take out the email that is the key.
    """
    groups = shelve.open("groups")
    f = open("p1.txt").readlines()
    num = 0
    for item in f:
        item = item.strip()
        a,b = item.split(",",1)
        c = b.split(",")
        for item in c:
            groups[item] = c

    groups.close()
    pass



def testing():
    gr = shelve.open("groups")
    print gr.keys()

def getRatings(email):
    quest = shelve.open("questions.dat")
    return quest[email]

def rate(email,quest,rate):
    quest = shelve.open("questions.dat")
    pass

createGroups()
fixNames()
#makeAuth()
print getRatings('batya.zamansky@gmail.com')

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
    f = open(data).readlines()
    print f
      
    pass

def createQuestions(data):
    """
    Makes the Questions shelve
    """

    pass

createGroups("p1.txt")

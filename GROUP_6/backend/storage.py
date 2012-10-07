import shelve
import os

if not os.path.isfile('info.dat'):
    s = shelve.open('info.dat')
    firre = open('students.txt')
    s['names'] = []
    s['ID'] = []
    s['period'] = []
    s['responses'] = []
    names = []
    ID = []
    period = []
    group = []
    responses = []
    for line in firre.readlines():
        currentstudent = line.split(',')
        ID.append(currentstudent[0])
        names.append(currentstudent[2] + " " + currentstudent[1])
        period.append(currentstudent[4])
        responses.append([])
    s['ID'] = ID
    s['names'] = names
    s['period'] = period
    s['group'] = group
    s['responses'] = responses

def addRating(email, rating):
    index = s['ID'].index(email)
    responses = s['responses'] 
    responses[index].append(rating)
    s['responses'] = responses

def getInfo(email):
    index = s['ID'].index(email)
    ret = []
    ret.append(s['names'][index])
    ret.append(s['period'][index])    
    ret.append(s['group'][index])
    ret.append(s['responses'][index])
    return ret

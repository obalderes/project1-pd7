import shelve
import os
s = shelve.open('info.dat')
def init():
    #if not os.path.isfile('info.dat'):

    firre = open('students.txt')
    name = []
    ID = []
    period = []
    group = []
    responses = []
    for line in firre.readlines():
        currentstudent = line.split(',')
        ID.append(currentstudent[0])
        name.append(currentstudent[2] + " " + currentstudent[1])
        period.append(currentstudent[6])
        group.append(currentstudent[7])
        responses.append([])
    s['ID'] = ID
    s['name'] = name
    s['period'] = period
    s['group'] = group
    s['responses'] = responses
    print s
#else:
 #       s = shelve.open('info.dat')

def addRating(email, rating):
    ids = s['ID']
    index = ids.index(email)
    responses = s['responses'] 
    responses[index].append(rating)
    s['responses'] = responses

def getInfo(email):
    ids = s['ID']
    index = ids.index(email)
    ret = []
    ret.append(s['name'][index])
    ret.append(s['period'][index])    
    ret.append(s['group'][index])
    ret.append(s['responses'][index])
    return ret
init()
#print s
addRating('a455898334@gmail.com', '5 stars')
#print s
getInfo('a455898334@gmail.com')
#print s


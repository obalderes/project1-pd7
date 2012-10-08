import shelve
import os
#<<<<<<< HEAD
s = shelve.open('info.dat')
def init():
    #if not os.path.isfile('info.dat'):

    firre = open('students.txt')
#=======

#if not os.path.isfile('info.dat'):
s = shelve.open('info.dat')
firre = open('students.txt')
s['ID'] = []
s['name'] = []
s['period'] = []
s['group'] = []
s['responses'] = []
#>>>>>>> 5e8ed64946a08b1cc3fb440b8bf8b4ed83e2ee30
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
#<<<<<<< HEAD
#print s
#else:
 #       s = shelve.open('info.dat')
#=======
#>>>>>>> 5e8ed64946a08b1cc3fb440b8bf8b4ed83e2ee30

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
#<<<<<<< HEAD
init()
#print s
#=======

#print s
#>>>>>>> 5e8ed64946a08b1cc3fb440b8bf8b4ed83e2ee30
addRating('a455898334@gmail.com', '5 stars')
#print s
getInfo('a455898334@gmail.com')
#print s


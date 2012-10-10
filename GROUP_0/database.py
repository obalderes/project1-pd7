import shelve, os

def getRatings(email):
## fix hardcoded 4s
    quesNum,projNum = 4,4
    l=[]
    for proj in range(projNum):
        l.append([])
        for ques in range(quesNum):
            l[proj].append([])
            
    for key in d[email][-1]:
        for ind, rating in enumerate(d[email][-1][key]):
            l[int(key[-1])-1][ind].append(rating)
    return l

def isUsername(email):
    for member in d:
        if member == email:
            return True
    return False

def getRatees(email):
    t = (d[email][5:7])
    l=[]
    for member in d:
        if d[member][5:7] == t and member != email:
            l.append(member)
    return l

def getName(email):
#return [first, last]
    s=d[email][0:2]
    s.reverse()
    return s

def getCurrentProject():
#returns top project number in projects.txt
    s=open('projects.txt').readline()
    return s[-6]

def setRatings(email,ratings):
#updates ratings
#ratings- [rating]
    return

if not os.path.isfile('data') or True:
    d = shelve.open('data',writeback=True)
    for line in open('students.txt'):   
        email,last,first,ID,course,courseNum,period,group = line.strip().split(',')
        receivedRatings = {}
        givenRatings = {}
        d[email]=[last,first,ID,course,courseNum,period,group,givenRatings,receivedRatings]
else:
    d = shelve.open('data')


#d['ste920ven@gmail.com'][-1]['TEST1']= [1,2,3,4]
#d['ste920ven@gmail.com'][-1]['QWERTY1']= [4,5,6,9]
#d['ste920ven@gmail.com'][-1]['ASDF1']= [7,8,9,3]


#print getCurrentProject()
#print isUserName('ste90ven@gmail.com')

d.close()

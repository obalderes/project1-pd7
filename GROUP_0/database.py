import shelve, os

def getRatings(email):
    quesNum,projNum = 7,getCurrentProject(email)
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

def getCurrentProject(email):
#returns top project number in projects.txt
    s=open('projects.txt').readline()
    return int(s[-6])

def setRatings(email,ratings, qnum):
#MOST LIKELY DOES NOT WORK
    #print ratings
    for member in ratings:
        for rating in ratings[member]:
            for n in range(qnum):
                ratings[member][n] = int(ratings[member][n])
        s= member + str(getCurrentProject(email))
        d[email][-2][s] = ratings[member]
        d[member][-1][s] = ratings[member]
            
if not os.path.isfile('data'):
    d = shelve.open('data',writeback=True)
    for line in open('students.txt'):   
        email,last,first,ID,course,courseNum,period,group = line.strip().split(',')
        receivedRatings = {}
        givenRatings = {}
        d[email]=[last,first,ID,course,courseNum,period,group,givenRatings,receivedRatings]
else:
    d = shelve.open('data',writeback=True)

#Tests
#d['ste920ven@gmail.com'][-1]['TEST1']= [1,2,3,4,5,6,7]
#d['ste920ven@gmail.com'][-1]['QWERTY1']= [4,5,6,9,1,8,7]
#d['ste920ven@gmail.com'][-1]['ASDF1']= [7,8,9,3,2,2,2]

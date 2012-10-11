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

def setRatings(email,ratings):
    print ratings
    for proj in ratings:
        for member in ratings[proj]:
            for rating in ratings[proj][member]:
                ratings[proj][member][rating] = int(ratings[proj][member][rating])
                print int(rating)
            s= member + str(proj)
            d[email][-2][s] = ratings[proj][member]
            d[member][-1][s] = ratings[proj][member]
    return

if not os.path.isfile('data'):
    d = shelve.open('data',writeback=True)
    for line in open('students.txt'):   
        email,last,first,ID,course,courseNum,period,group = line.strip().split(',')
        receivedRatings = {}
        givenRatings = {}
        d[email]=[last,first,ID,course,courseNum,period,group,givenRatings,receivedRatings]
else:
    d = shelve.open('data',writeback=True)


#d['ste920ven@gmail.com'][-1]['TEST1']= [1,2,3,4,5,6,7]
#d['ste920ven@gmail.com'][-1]['QWERTY1']= [4,5,6,9,1,8,7]
#d['ste920ven@gmail.com'][-1]['ASDF1']= [7,8,9,3,2,2,2]

#a = {3:{'Hayden.kh@gmail.com':[1,2,3,4]},1:{'jskestrel@aol.com':[5,6,7,8]}}

#print setRatings('ste920ven@gmail.com', a)
#print d['ste920ven@gmail.com'][-2]
#print d['Hayden.kh@gmail.com'][-1]
#print d['jskestrel@aol.com'][-1]
#print getRatings('jskestrel@aol.com')

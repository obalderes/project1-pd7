import shelve, os

def getRatings(email):
#return {rater: [rating]}
    return d[email][-1]

def isUserName(email):
#check is usuername exists
    for member in d:
        if member == email:
            return True
    return False

def getRatees(email):
#return [member]
    t = (d[email][5:7])
    l=[]
    for member in d:
        if d[member][5:7] == t and member != email:
            l.append(member)
    return l

def getName(email):
#return [ID, first, last]
    s=d[email][0:3]
    s.reverse()
    return s

def setRatings(email,ratings):
#updates ratings
#ratings- [rating]
    return

if not os.path.isfile('data'):
    d = shelve.open('data')
    for line in open('students.txt'):   
        email,last,first,ID,course,courseNum,period,group = line.strip().split(',')
        receivedRatings = {}
        givenRatings = {}
        d[email]=[last,first,ID,course,courseNum,period,group,givenRatings,receivedRatings]
else:
    d = shelve.open('data')
    
print getRatees('ste920ven@gmail.com')
print isUserName('ste90ven@gmail.com')

d.close()

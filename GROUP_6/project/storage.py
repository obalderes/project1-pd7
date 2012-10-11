import shelve
import os

if not os.path.isfile('info.dat'):
    s = shelve.open('info.dat')
    firre = open('students.txt')
    name = []
    ID = []
    period = []
    group = []
    rating1 = []
    rating2 = []
    rating3 = []
    rating4 =[]
    comment = []
    rater = []
    for line in firre.readlines():
        currentstudent = line.split(',')
        ID.append(currentstudent[0])
        name.append(currentstudent[2] + " " + currentstudent[1])
        period.append(currentstudent[6])
        group.append(currentstudent[7][1:2])
        rating1.append([])
        rating2.append([])
        rating3.append([])
        rating4.append([])
        comment.append([])
        rater.append([])
    s['ID'] = ID
    s['name'] = name
    s['period'] = period
    s['group'] = group
    s['rating1'] = rating1
    s['rating2'] = rating2
    s['rating3'] = rating3
    s['rating4'] = rating4
    s['comment'] = comment
    s['rater'] = rater
else:
    s = shelve.open('info.dat')

def addRating(_ratee, _rater, _rating1, _rating2, _rating3,_rating4, _comment):
    if not _rater in s['rater'][s['ID'].index(_ratee)]:
        ids = s['ID']
        index = ids.index(_ratee)
        rating1 = s['rating1'] 
        rating2 = s['rating2'] 
        rating3 = s['rating3']
        rating4 = s['rating4']
        comment = s['comment']
        rater = s['rater']  
        rating1[index].append(_rating1)
        rating2[index].append(_rating2)
        rating3[index].append(_rating3)
        rating4[index].append(_rating4)
        comment[index].append(_comment)
        rater[index].append(_rater)
        s['rating1'] = rating1
        s['rating2'] = rating2
        s['rating3'] = rating3
        s['rating4'] = rating4
        s['comment'] = comment
        s['rater'] = rater

def getInfo(email):
    index = s['ID'].index(email)
    ret = []
    ret.append(s['name'][index])
    ret.append(s['period'][index])    
    ret.append(s['group'][index])
    ret.append(s['rating1'][index])
    ret.append(s['rating2'][index])
    ret.append(s['rating3'][index])
    ret.append(s['rating4'][index])
    ret.append(s['comment'][index])
    ret.append(s['rater'][index])
    return ret

def checkUser(email):
    for emails in s['ID']:
        if emails == email:
            return True
    return False

def returnIDlist():
    return s['ID']
def returnGroupList(email):
    Group = []
    ID = getInfo(email)
    IDClassList = returnIDlist()
    for mate in IDClassList:
        if ID[2] == getInfo(mate)[2] and email != mate and ID[1] == getInfo(mate)[1]:
            Group.append(mate)
    return Group
    

if __name__ == "__main__":
    #print s
    #addRating('a455898334@gmail.com','rybicka.zuzanna@gmail.com','5','6','7','8','coolest person on earth')
    #addRating('a455898334@gmail.com','sorakeybade@gmail.com','9','8','7','8','coolest person on earth')
    #print s
    #print getInfo('a455898334@gmail.com')
    #print s['group']
    print returnGroupList('sorakeybade@gmail.com')
    print len(returnGroupList('sorakeybade@gmail.com'))

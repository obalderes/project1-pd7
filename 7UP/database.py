"""
2 Dictionary Structure
database(s) of Projects(d) and People(d)
each projects(d) of groups(d)
each groups(d) of members
"""

import shelve

database = shelve.open('database.dat', writeback=True)

#    creates new entry for Project(d) given data for that project
#    in groups, emails are keys pointing to a dictionary of their data

def createProj(data):
    p = dict([(i,{}) for i in range(0,15)])
    emails = open(data)
    
    for line in emails:
        x,y = str(line.strip()).split(",",1)
        y = y.split(",")
        p[int(x)] = dict([(i,{}) for i in y])

    people = returnPeopleDict()
    
    for x in p: 
        for person in p[x]:
            tempList = people[person]
            p[x][person] = {'first':tempList[0],'last':tempList[1],'email':person,'feedback':{}}
            
    return p

# returns dictionary of all students and their info
def returnPeopleDict(): 
    s = open('students.txt')
    people = {} 
    for line in s:
        email,last,first,ID,className,classNumber,Period,GroupNumber = str(line.strip()).split(",",7)
        people[email] = [first,last,email,{}]

    return people


#returns a project dictionary given project number
def getProject(projnumber):
    return database['Projects'][int(projnumber)]

#returns group given project and group number
def getGroup(projnumber,groupnumber):
    p = getProject(projnumber)
    return p[int(groupnumber)]




projects = {}
database['Projects'] = projects
projects['1'] = createProj('p1.txt')

print database['Projects']['1'][0]['ericc6134@gmail.com']
print database['People']['raymondzzzeng@gmail.com']
database.close()

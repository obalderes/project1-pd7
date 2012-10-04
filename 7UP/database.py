"""
2 Dictionary Structure
database(s) of Projects(d) and People(d)
each projects(d) of groups(d)
each groups(d) of members
"""

import shelve

database = shelve.open('database.dat', writeback=True)

def createProj(data):
    """
creates new entry for Project(d) given data for that project
in groups, emails are keys pointing to none
- none to be replaced with members
"""
    p = dict([(i,{}) for i in range(0,15)])
    emails = open(data)
    
    for line in emails:
        x,y = str(line.strip()).split(",",1)
        y = y.split(",")
        p[int(x)] = dict([(i,{}) for i in y])

    people = returnPeopleDict()
    for x in p: #for every group in projects(d)
        for person in p[x]:
            tempList = people[person]
            p[x][person] = {'first':tempList[0],'last':tempList[1],'email':person,'feedback':{}}
            
    return p

def returnPeopleDict(): # set up the people dictionary
    s = open('students.txt')
    people = {} 
    for line in s:
        email,last,first,ID,className,classNumber,Period,GroupNumber = str(line.strip()).split(",",7)
        people[email] = [first,last,email,{}]

    return people
                
projects = {}
database['Projects'] = projects
projects['1'] = createProj('p1.txt')

print database['Projects']['1'][0]
database.close()

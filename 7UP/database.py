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
        p[int(x)] = dict([(i,'none') for i in y])
 
    return p

projects = {}
projects['1'] = createProj('p1.txt')
database['Projects'] = projects

print database['Projects']['1'][0]
database.close()

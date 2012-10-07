

import shelve

database = shelve.open('database.db', writeback=True)
#d = shelve.open("students.dat")
#I can't figure out the shelf implementation... I keep on getting a "db" type error so I'm just going to program instantiating a dictionary instead.

#If you change db (I don't know what this is) to .dat, it works but idk if you specifically needed a db type

s = open('students.txt')
y = open('students.txt')
people = {}
projx = {}
groupnumbers = []

#creates a dictionary of people each with empty spaces for projects, groups in projects, and members in groups
def setupPeople():
    for line in s:
        email,last,first,ID,className,classNumber,Period,Gnuminclass,gnum = str(line.strip()).split(",",8)
        projects = {}
        people[email] = [first,last,email,projects,ID,className,classNumber,Period,gnum,Gnuminclass]
        if groupnumbers.count(gnum) == 0:
            groupnumbers.append(gnum)
    for person in people:
         projects = {}
         groups = {}
         members = {}
         projects['groups'] = groups
         groups['members'] = members
          
#adds a new project to a person and gives them access to the emails of their group members for that project  
def addProjectToPerson(emailaddress,projectname):
    people[emailaddress][3][projectname] = {}
    theirgroup = people[emailaddress][8]
    for g in groupnumbers:
        people[emailaddress][3][projectname][g] = []
    for email in people:
        currentgroup = people[email][8]
        if (((int)(currentgroup) == 15) and (people[email] != people[emailaddress])):
            people[emailaddress][3][projectname][theirgroup].append(people[email])

#creates a dictionary of projects with groups and all the members of the groups, and an empty dictionary for their feedback. Used for individuals to look up their own data
def setupProject():
    groupnums = []
    membs = {}
    for line in y:
        email,last,first,ID,className,classNumber,Period,Gnuminclass,gnum = str(line.strip()).split(",",8)
        if groupnums.count(gnum) == 0:
            groupnums.append(gnum)
    projx['project one'] = groupnumbers
    for grps in groupnumbers:
        projx['project one'][(int)(grps)] = {}
    for person in people:
        theirgroup = people[person][8]
        projx['project one'][(int)(theirgroup)][person] = {}
    print projx['project one'][15]

        
def returnPeopleDict(): # set up the people dictionary
    return people

setupPeople()
setupProject()
#addProjectToPerson("iouthwaite1@gmail.com",'newproject')
#database = [project,people]






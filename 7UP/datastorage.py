
#
import shelve

database = shelve.open('database.dat', writeback=True)
#d = shelve.open("students.dat")
#I can't figure out the shelf implementation... I keep on getting a "db" type error so I'm just going to program instantiating a dictionary instead.

#If you change db (I don't know what this is) to .dat, it works but idk if you specifically needed a db type

s = open('students.txt')
people = {}
groupnumbers = []

def setupPeople():
    # set up the people dictionary
    for line in s:
        email,last,first,ID,className,classNumber,Period,GroupNumber = str(line.strip()).split(",",7)
        projects = {}
        people[email] = [first,last,email,projects,ID,className,classNumber,Period,GroupNumber]
        if groupnumbers.count(GroupNumber) == 0:
            groupnumbers.append(GroupNumber)
    print people['iouthwaite1@gmail.com']
    for person in people:
         projects = {}
         groups = {}
         members = {}
         projects['groups'] = groups
         groups['members'] = members
            
def addProjectToPerson(emailadress,projectname):
    for email in people:
        if email==emailadress:
            people[email][3][projectname] = {}
            for g in groupnumbers:
                people[email][3][projectname][g] = {}
            print people[email][3][projectname]
    


setupPeople()   
addProjectToPerson("iouthwaite1@gmail.com",'newproject')         
#database = [project,people]
            
            

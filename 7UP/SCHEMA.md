Group 7UP
=========

* * *

## SCHEMA ##

Shelf containing a dictionary of "projects" and a dictionary of "people"

## PROJECTS ##
* each project contains a dictionary of "groups"
* each group contains a dictionary of "members" 
* each member has a name(first,last), and an email adress, and a dictionary of feedback
* each entry in feedback is a list of length 4, with room for the period,group,score,and comments.

## PEOPLE ##
* each person has a name(first,last) an email adress, and a dictionary of "projects1"
* Projects1 is a dictionary that contains a list of groups
* each group contains a dictionary of "groupmems"
* each groupmem has a name(first,last), an email adress, and list of questions. (It refers to the member within projects)
* each question is a list of length 4, with room for one score and one comment (project# and group# are automatically added)

The basic idea is that in our program a user will search themselves up to get their own scores through "PROJECTS," and they will give feedback to to others through the "PEOPLE" dictionary.

STUFF TO COPY PASTE

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
    # print people['iouthwaite1@gmail.com']
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
                people[email][3][projectname][g] = []
            # print people[email][3][projectname]
            for email in people:
                currentgroup = people[email][8]
                if ((int)(currentgroup) == 1):
                    if (people[email] != people[emailadress]):
                        people[emailadress][3][projectname][currentgroup].append(people[email])
            for email in people:
                currentgroup = people[email][8]
                print currentgroup
                print people[emailadress][3][projectname][currentgroup]
                    #people[emailadress][3][projectname][currentgroup][email] = people[email]
            
        
    


setupPeople()
addProjectToPerson("iouthwaite1@gmail.com",'newproject')
#database = [project,people]

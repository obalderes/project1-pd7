import shelve

database = shelve.open('database.dat', writeback=True)

people = {}
projx = {}
groupnumbers = []

#creates a dictionary of people each with empty spaces for projects, groups in projects, and members in groups
#people -> projects -> groups -> members
def setupPeople():
    z = open('students.txt')
    for line in z:
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
    if groupnumbers.count(gnum) == 0:
        groupnumbers.append(gnum)
    for g in groupnumbers:
        people[emailaddress][3][projectname][g] = []
    for email in people:
        currentgroup = people[email][8]
        if (((int)(currentgroup) == 15) and (people[email] != people[emailaddress])):
            people[emailaddress][3][projectname][theirgroup].append(people[email])

#creates a new project within the projx overarching dictionary. Fills it in with the groups, members of each group, and space in each member's location for feedback.
#projects -> groups for that project -> memebers
def createNewProject(projectname):
    z = open('students.txt')
    groupnums = []
    membs = {}
    for line in z:
        email,last,first,ID,className,classNumber,Period,Gnuminclass,gnum = str(line.strip()).split(",",8)
        if groupnums.count(gnum) == 0:
            groupnums.append(gnum)
    projx[projectname] = groupnums
    for grps in groupnums:
        projx[projectname][(int)(grps)] = {}
    for person in people:
        theirgroup = people[person][8]
        projx[projectname][(int)(theirgroup)][person] = []
    projx['currentproject'] = projectname

def getFirst(emailadd):
    return people[emailadd][0]

def getLast(emailadd):
    return people[emailadd][1]


        
def returnPeopleDict():
    return people

#returns a list of their data, project->data from each project
def getData(emailaddress):
    data = []
    for projs in projx:
        for groops in projx[projs]:
            for person in groops:
                if person == emailaddress:
                    data.append(projx[projs][(int)(people[person][8])][person])
    return data

#rates a person in your group and in your current project
def ratePerson(rater,ratee,question,score,comments):
    data = {}
    data['rater'] = rater
    data['question'] = question
    data['score'] = score
    data['comments'] = comments
    CurrProj = projx["currentproject"]
    CurrGroup = people[rater][8]
    projx[CurrProj][(int)(CurrGroup)][ratee].append(data)   

setupPeople()
createNewProject('2')
createNewProject("1")
print getData('iouthwaite1@gmail.com')
print getFirst('iouthwaite1@gmail.com')
print getLast('iouthwaite1@gmail.com')

#addProjectToPerson("iouthwaite1@gmail.com",'newproject')
ratePerson("iouthwaite1@gmail.com","Oneman2feet@gmail.com","Do you like pizza", 5, "eat it all day")
ratePerson("raymondzzzeng@gmail.com","Oneman2feet@gmail.com","Do you like pizza", 5, "eat it all day")
print getData("Oneman2feet@gmail.com")
#database = [project,people]

database['People'] = people
database['Projects'] = projx

#returns sorted list ranking students for a given project and given question
def getRankings(question,projnum):
    project = database['Projects'][projnum]
    rankings = []
    for group in project:
        for member in group:
            for info in member:
                if (project[group][member][info]['question'] == question):
                    t = project[group][member]['data']['score'], project[group][member]['email']
                    rankings.append(t)
            
               
    rankings.sort()
    return rankings

#print database['Projects']['1']
print getRankings('Do you like pizza','1')
database.close()






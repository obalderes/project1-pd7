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

def getAvgForQuestion(email,projnum,q):
    data = getData(email)[int(projnum)]
    temp = []
    if len(data) == 0:
        return 0
    
    for d in data:
        if d['question'] == str(q):
            temp.append(d)
            
    if len(temp) == 0:
        return 0
    
    sum = 0        
    for dict in temp:
        sum = sum + dict['score']
        
    return sum / len(temp)
        
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

print getFirst('iouthwaite1@gmail.com')
print getLast('iouthwaite1@gmail.com')

#addProjectToPerson("iouthwaite1@gmail.com",'newproject')
ratePerson("iouthwaite1@gmail.com","Oneman2feet@gmail.com","Do you like pizza", 5, "eat it all day")
ratePerson("raymondzzzeng@gmail.com","Oneman2feet@gmail.com","Do you like pizza", 5, "eat it all day")
ratePerson("iouthwaite1@gmail.com","raymondzzzeng@gmail.com","Do you like pizza", 3,"m")
ratePerson("Oneman2feet@gmail.com","raymondzzzeng@gmail.com","Do you like pizza",1, "m")
ratePerson("raymondzzzeng@gmail.com","iouthwaite1@gmail.com","Do you like pizza", 4, "m")
ratePerson("raymondzzzeng@gmail.com","bdh227@gmail.com","Do you like pizza", 3, "m")
#print getData("Oneman2feet@gmail.com")

database['People'] = people
database['Projects'] = projx

#returns list of tuples (Avg rating, email)
#return[0] has the highest rating
#input: Project number where the first project is indexed by 0
def getRankings(projnum,question):
    people = database['People']
    rankings = []
    for person in people:
        t = (getAvgForQuestion(person,projnum,question), person)
        rankings.append(t)            
    rankings.sort()

    temp = []
    for i in reversed(rankings):
        temp.append(i)
        
    return temp


print getRankings('0',"Do you like pizza")
database.close()






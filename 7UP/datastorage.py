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
    if groupnumbers.count(theirgroup) == 0:
        groupnumbers.append(theirgroup)
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


#returns a list of the group members not including the individual
# Ex: If you're Bobby Joe, you might see ['Will Smith', 'Harry Fontane', 'Bobby Banjo']
def getGroupMembers(emailad,project):
    temp = []
    for person in people[emailad][3][project][people[emailad][8]]:
        temp.append(person[0] + " " + person[1])
    #for person in people[emailad][3][project][people[emailad][gnum]]:
    #    temp.append(person[1] + " " + person[0])
    return temp


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

setupPeople()
createNewProject('2')
createNewProject("1")
addProjectToPerson('iouthwaite1@gmail.com','1')
print getGroupMembers('iouthwaite1@gmail.com','1')

database['People'] = people
database['Projects'] = projx

database.close()






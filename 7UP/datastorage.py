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

def getTotalIndividualAvgForQuestion(emailadd,ques):
    temp = getData(emailadd)[0]
    x = 0.0
    count = 0.0
    for response in temp:
        if (response['question'] == ques):
            x = x + response['score']
            count = count + 1
    if (count==0):
        return 0
    return x/count

def getTotalIndividualPointsForQuestion(emailadd,ques):
    temp = getData(emailadd)[0]
    x = 0
    for response in temp:
        if (response['question'] == ques):
            x = x + response['score']
    return x

def getTotalGroupAvgForQuestion(ques):
    x = 0.0
    count = 0.0
    for person in people:
        temp = getData(person)
        for entry in temp:
            if (entry != []):
                for response in entry:
                    if (response['question'] == ques):
                        x = x + response['score']
                        count = count + 1 
    if (count == 0):
        return 0
    return x/count 

def getTotalGroupOverallAvg():
    x = 0.0
    count = 0.0
    for person in people:
        temp = getData(person)
        for entry in temp:
            if (entry != []):
                for response in entry:
                    x = x + response['score']
                    count = count + 1
    if (count == 0):
        return count
    return x/count
    
def getTotalOverallIndividualPoints(emailadd):
    x = 0
    temp = getData(emailadd)
    for entry in temp:
        if (entry != []):
            for response in entry:
                x = x + response['score']
    return x    

def getAvgOverallIndividualPoints(emailadd):    
    x = 0.0
    count = 0.0
    temp = getData(emailadd)
    for entry in temp:
        if (entry != []):
            for response in entry:
                x = x + response['score']
                count = count + 1
    if (count == 0):
        return 0
    return x/count       
                  
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
def getRankings(question):
    people = database['People']
    rankings = []
    for person in people:
        t = (getTotalIndividualAvgForQuestion(person,question), person)
        rankings.append(t)            
    rankings.sort()

    temp = []
    for i in reversed(rankings):
        temp.append(i)
    return temp

def getTopTen(question):
    rankings = getRankings(question)
    rankings = rankings[:10]
    return rankings





#checks to see if entered name is a user, returns 0 for false and 1 for true
def isUser(emailadd):
    for person in people:
        if (people[person][2] == emailadd):
            return 1
    return 0
        
            

setupPeople()
createNewProject('2')
createNewProject("1")
addProjectToPerson('iouthwaite1@gmail.com','1')
addProjectToPerson('Oneman2feet@gmail.com','1')
ratePerson('iouthwaite1@gmail.com','Oneman2feet@gmail.com','question?',5,'it was lovely')
ratePerson('iouthwaite1@gmail.com','Oneman2feet@gmail.com','bladsalfa',5,'it was lovely')
addProjectToPerson('Oneman2feet@gmail.com','2')
ratePerson('iouthwaite1@gmail.com','Oneman2feet@gmail.com','question?',3,'marrrr')

print getTotalOverallIndividualPoints('Oneman2feet@gmail.com')
print getTotalIndividualPointsForQuestion('Oneman2feet@gmail.com','question?')
print getAvgOverallIndividualPoints('Oneman2feet@gmail.com')
print getTotalIndividualAvgForQuestion('Oneman2feet@gmail.com','question?')

print getTotalGroupOverallAvg()
print getTotalGroupAvgForQuestion('question?')

#print getRankings('question?')
print getTopTen('question?')


#print getGroupMembers('iouthwaite1@gmail.com','1')
#print isUser('iouthwaite1@gmail.com')
#print isUser('toad')

database['People'] = people
database['Projects'] = projx

database.close()






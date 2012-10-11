import shelve

#Have to use try-except statements because the way file paths worked
#in Windows and in Linux/Mac were different. This should have fixed
#the problem
#-Brian Lam
try:
    Students = open("students.txt", "r").readlines()
except Exception:
    Students = open("/students.txt", "r").readlines()

try:
    groupShelve = shelve.open("groupShelves")
except Exception:
    try:
        groupShelve = shelve.open("groupShelves.dat")
    except Exception:
        groupShelve = shelve.open("/groupShelves")

try:
    studentShelve = shelve.open("studentShelves")
except Exception:
    try:
        studentShelve = shelve.open("/studentShelves")
    except Exception:
        tudentShelve = shelve.open("studentShelves.dat")

responseShelve = shelve.open("responseShelve.dat")

#Check if shelve has been created so the program doesn't create a new shelf
#each time- Brian Lam's version
try:
    if studentShelve["createdCheck"] == "shelve has been created":
        print "Shelve has already been created. Will not compile new shelve"
except Exception:
    print "Shelve hasn't been created yet. Creating shelf now."
    for student in Students:
        student = student.strip()
        email,lastname,firstname,idnumber,course,ignore,period,group=student.split(",")
        group = group.strip()
        studentShelve[email]=email+","+lastname+","+firstname+","+idnumber+","+period+","+group
        print studentShelve[email]
    studentShelve["createdCheck"] = "shelve has been created"
    print "Shelve has been compiled"


#Check if the email is in the email list - Brian Lam's version
#Largely based off of Mengdi's version of this, many thanks to
#her for providing a guideline on the try-except block
def emailAuth(email):
    try:
        studentShelve[email]
        return True
    except Exception:
        return False

#Takes rater's name, ratee's name question ID, and rating value and stores it
#Mengdi Lin's version
def add_rating(rater,ratee,question,rating):
    students = shelve.open("students",writeback=True) 
    total_question=9
    index =int(float(question[1:]))-1
    if(students[rater]["Group"]==students[ratee]["Group"]):
        if(rater not in students[ratee]["Rating Received"].keys() and ratee not in students[rater]["Rating Given"].keys()):
            students[ratee]["Rating Received"][rater]=['-1']*total_question
            students[rater]["Rating Given"][ratee]=['-1']*total_question
        students[ratee]["Rating Received"][rater][index]=rating
        students[rater]["Rating Given"][ratee][index]=rating
        return True
    else:
        return False
    students.close()

#Returns a list of the ratings of a user, given the user's email
#Mengdi Lin's version
def get_rating(user,type_rating):
    students = shelve.open("students",writeback=True) 
    d=[]
    for key in students[user][type_rating].keys():
        for index in range(len(students[user][type_rating][key])):
            if(students[user][type_rating][key][index]!='-1'):
                q='q0'+str(index+1)
                tmp=q+user+'/'+students[user][type_rating][key][index]
                d.append(tmp)
    students.close()
    return d

#Brian Lam's version of response saving
def save_response(email,response):
    responseShelve[email]=response

#Brian Lam's verison of response retrieval
def get_response(email):
    try:
        return responseShelve[email]
    except Exception:
        return ""
    

#Brian Lam's version
def userFirst(email):
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return firstname

#Brian Lam's version
def userLast(email):
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return lastname

#Brian Lam's version
def userIdNumber(email):
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return idnumber

#Brian Lam's version
def userPeriod(email):
    email = str(email)
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return period

#Brian Lam's version
def userGroup(email):
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return group

#Brian Lam's version
def userGroupMembers(email):
    L = []
    email = str(email)
    groupnumber = userGroup(email)
    periodnumber = userPeriod(email)
    for student in Students:
        student = student.strip()
        studentemail,lastname,firstname,idnumber,course,ignore,period,group=student.split(",")
        group = group.strip()
        if(period == periodnumber and group == groupnumber and studentemail != email):
            L.append(studentemail)
    return L


#Compiles the shelve of students, keyed by their emails, containing other information
#separated by commas
#Brian Lam's version
def compileShelve():
    for student in Students:
        student = student.strip()
        email,lastname,firstname,idnumber,course,ignore,period,group=student.split(",")
        group = group.strip()
        studentShelve[email]=email+","+lastname+","+firstname+","+idnumber+","+period+","+group

import shelve

Students = open("students.txt", "r").readlines()

groupShelve = shelve.open("groupShelves")
studentShelve = shelve.open("studentShelves")

#Check if shelve has been created
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


def emailAuth(email):
    try:
        studentShelve[email]
        return True
    except Exception:
        return False

def userFirst(email):
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return firstname

def userLast(email):
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return lastname

def userIdNumber(email):
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return idnumber

def userPeriod(email):
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return period

def userGroup(email):
    student = studentShelve[email]
    email,lastname,firstname,idnumber,period,group = student.split(",")
    return group

def userGroupMembers(email):
    L = []
    groupnumber = userGroup(email)
    periodnumber = userPeriod(email)
    for student in Students:
        student = student.strip()
        studentemail,lastname,firstname,idnumber,course,ignore,period,group=student.split(",")
        group = group.strip()
        if(period == periodnumber and group == groupnumber):
            L.append(studentemail)
    return L
        
     
def compileShelve():
    for student in Students:
        student = student.strip()
        email,lastname,firstname,idnumber,course,ignore,period,group=student.split(",")
        group = group.strip()
        studentShelve[email]=email+","+lastname+","+firstname+","+idnumber+","+period+","+group

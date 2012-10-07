#!/usr/bin/python 

import shelve

#### students.db ####

def retrieveStudentInfo(email):
    studentDatabase = shelve.open("students.db")
    studentInfo = studentDatabase[email]
    if studentInfo == []:
        return False
    else:
        return studentInfo
    studentDatabse.close()


#### groups.db ####

def membersInGroup(groupNumber):
    groupDatabase = shelve.open("groups.db")
    groupMembers = groupDatabase[groupNumber]
    if groupMembers == []:
        return False
    else:
        return groupMembers
    groupDatabase.close()

def getGroupNumber(email):
    studentInfo = retrieveStudentInfo(email)
    groupNumber = studentInfo[6]
    return groupNumber

def retrieveGroupMembers(email):
    groupNumber = getGroupNumber(email)
    groupMembers = membersInGroup(groupNumber)
    return groupMembers



#### grades.db ####

def retrieveGrades(email):
    gradesDatabase = shelve.open("grades.db")
    grades = gradesDatabase[email]
    if grades == []:
        return False
    else:
        return grades
    gradesDatabase.close()

def setGrades(grades,email):
    gradesDatabase = shelve.open("grades.db")
    gradesList = gradesDatabase[email]
    question = 0
    for question in gradesList:
        question.append[grades[question]]
        question = question + 1
    
    gradesDatabase.close()



#### ratedBy.db ####
   
def addRatedBy(targetEmail,graderEmail):
    ratedByDatabase = shelve.open("ratedBy.db")
    ratedByDatabase[targetEmail].append(graderEmail)
    ratedByDatabase.close()

def hasBeenRatedBy(targetEmail,graderEmail):
    ratedByDatabase = shelve.open("ratedBy.db")
    ratedBy = ratedByDatabase[targetEmail]
    if graderEmail in ratedBy:
        return True
    else:
        return False

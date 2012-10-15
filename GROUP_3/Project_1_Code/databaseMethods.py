#!/usr/bin/python 

import shelve
#import shelveSetup






#### students.db ####


currentStudent = ""

def saveCurrentStudent(email):
    currentStudent = email

def getCurrentStudent():
    return currentStudent

def isAKey(email):
    studentDatabase = shelve.open("students")
    if studentDatabase.has_key(email):
        return True
    else:
        return False
    studentDatabase.close()


def retrieveStudentInfo(email):
    studentDatabase = shelve.open("students")
    studentInfo = studentDatabase[email]
    return studentInfo
    studentDatabase.close()


#### groups.db ####

def membersInGroup(groupNumber):
    groupDatabase = shelve.open("groups")
    groupMembers = groupDatabase[groupNumber.strip()]
    return groupMembers
    groupDatabase.close()

def getGroupNumber(email):
    studentInfo = retrieveStudentInfo(email)
    groupNumber = studentInfo[6]
    return groupNumber

def retrieveGroupMembers(email):
    groupNumber = isInGroupNumber(email)
    groupMembers = membersInGroup(groupNumber)
    return groupMembers



#### grades.db ####

def retrieveGrades(email):
    gradesDatabase = shelve.open("grades")
    grades = gradesDatabase[email]
    gradesDatabase.close()
    return grades

   

def setGrades(grades,email):
    gradesDatabase = shelve.open("grades")
    gradesList = gradesDatabase[email]
    for questionNum in range(0,4):
        toAppend = grades[questionNum]
        gradesList[questionNum].append(toAppend)
    
    gradesDatabase.close()



#### ratedBy.db ####
   
def addRatedBy(targetEmail,graderEmail):
    ratedByDatabase = shelve.open("ratedBy")
    ratedByDatabase[targetEmail].append(graderEmail)
    ratedByDatabase.close()

def hasBeenRatedBy(targetEmail,graderEmail):
    ratedByDatabase = shelve.open("ratedBy")
    ratedBy = ratedByDatabase[targetEmail]
    if graderEmail in ratedBy:
        return True
    else:
        return False


#### nameToGroupNumber ####

def isInGroupNumber(email):
    place = shelve.open("nameToGroupNumber")
    groupNumber = place[email]
    place.close()
    return groupNumber

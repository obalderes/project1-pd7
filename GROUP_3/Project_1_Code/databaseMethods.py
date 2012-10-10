#!/usr/bin/python 

import shelve
import shelveSetup






#### students.db ####


currentStudent = ""

def saveCurrentStudent(email):
    currentStudent = email

def getCurrentStudent():
    return currentStudent


def retrieveStudentInfo(email):
    studentDatabase = shelve.open("students")
    studentInfo = studentDatabase[email]
    if studentInfo == []:
        return False
    else:
        return studentInfo
    studentDatabase.close()


#### groups.db ####

def membersInGroup(groupNumber):
    groupDatabase = shelve.open("groups")
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
    gradesDatabase = shelve.open("grades")
    grades = gradesDatabase[email]
    gradesDatabase.close()
    return grades
   

def setGrades(grades,email):
    gradesDatabase = shelve.open("grades")
    gradesList = gradesDatabase[email]
    question = 0
    for question in gradesList:
        question.append[grades[question]]
        question = question + 1
    
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

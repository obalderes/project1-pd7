#!/usr/bin/python 

import shelve

#### students.db ####

def retrieveStudentInfo(email):
    studentDatabase = shelve.open("students.db")
    studentInfo = studentDatabase[email]
    if studentInfo eq []:
        return False
    else:
        return studentInfo
    studentDatabse.close()


#### groups.db ####

def retrieveGroupMembers(groupNumber): 
    groupDatabase = shelve.open("groups.db")
    groupMembers = groupDatabase[groupNumber]
    if groupMembers eq []:
        return False
    else:
        return groupMembers
    groupDatabase.close()



#### grades.db ####

def retrieveGrades(email):
    gradesDatabase = shelve.open("grades.db")
    grades = gradesDatabase[email]
    if grades = []:
        return False
    else:
        return grades
    gradesDatabase.close()

def setGrades(grades):
    gradesDatabase = shelve.open("grades.db")
    ###more goes here ###


#### ratedBy.db ####
   

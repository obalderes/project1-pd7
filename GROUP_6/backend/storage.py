import shelve
import os

if not os.path.isfile('info.dat'):
    s = shelve.open('info.dat')
    firre = open('students.txt')
    s['names'] = []
    s['ID'] = []
    s['period'] = []
    s['responses'] = []
    names = []
    ID = []
    period = []
    for line in firre.readlines():
        currentstudent = line.split(',')
        ID.append(currentstudent[0])
        names.append(currentstudent[2] + " " + currentstudent[1])
        period.append(currentstudent[4])
    s['ID'] = ID
    s['names'] = names
    s['period'] = period
    print s

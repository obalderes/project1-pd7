import shelve
import os
import file
if not os.path.isfile('info.dat'):
    s = shelve.open('info.dat')
    firre = file.open('students.txt')
    s['names'] = []
    s['ID'] = []
    s['responses'] = []
    names = []
    ID = []
    for line in firre.readlines():
        currentstudent = line.split(',')
        ID.append(currentstudent[0])
        names.append(currentstudent[2] + " " + currentstudent[1])
    s['ID'] = ID
    s['names'] = names
    print s

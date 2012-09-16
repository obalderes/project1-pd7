#this solution is probably much more complicated than is necessary

from random import randrange

names = []
#morenames = {}

f = open('ml7-student-names')

for line in f.readlines(): 
    names.append(line.strip()) #get the names and put them in a list

f.close()

pd6 = []
pd7 = []

#print names[5:13] #test

for name in names:
    if name not in pd6 and name not in pd7: #ignore repeats
        if '6' == name[-1]: #if person in pd 6
            pd6.append(name) #add to pd 6 
        else: pd7.append(name)

#print len(pd6),len(pd7) #test

groups6 = [] #keep a list of the groups for each period
groups7 = []

while len(pd6) > 0: #for all people in pd 6 
    group = []
    while len(group) < 4: #make groups of 4 people each
        name = pd6[randrange(0,len(pd6))] #get a random person from this period
        group.append(name) #add them to the group 
        pd6.remove(name) #remove them from the list (no repeats)
    groups6.append(group) #list of the groups in this period

while len(pd7) > 0: #same as above but for pd 7
    group = []
    while len(group) < 4:
        name = pd7[randrange(0,len(pd7))]
        group.append(name)
        pd7.remove(name)
    groups7.append(group)

print groups6 + groups7

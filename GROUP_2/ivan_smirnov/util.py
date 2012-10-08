QuestionsList = open("questions.txt", "r").readlines()

StudentsList = open("students.txt", "r").readlines()

def verifylogin(email, idnum):
    for n in StudentsList:
        if (email in n and idnum in n):
            return True
        else:
            return False

def get_group(email):
    for n in StudentsList:
        if (email in n):
            print str(n)[(len(str(n))-2):]

GroupsList = open("students.txt", "r").readlines()

g = []

for n in GroupsList:
    g.append(n.split(","))

def get_groupMembers(x):    #<--this method returns members from BOTH group x's
    for n in g:
        if(x in n[7]):
            print n[1] + "," + n[2]

def get_groupMembers(x,period):
    for n in g:
        if(x in n[7]):
            if(period in n[6]):
                print n[1] + "," + n[2]






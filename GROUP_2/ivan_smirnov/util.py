QuestionsList = open("questions.txt", "r").readlines()

#for n in QuestionsList:
    #print n

StudentsList = open("students.txt", "r").readlines()

def verifylogin(email, idnum):
    for n in StudentsList:
        if (email in n and idnum in n):
            print "true"
        else:
            print "false"
         
#verifylogin("ivansmirnov13@gmail.com","8231")

def get_group(email):
    for n in StudentsList:
        if (email in n):
            print str(n)[(len(str(n))-2):]

get_group("ivansmirnov13@gmail.com")

GroupsList = open("students.txt", "r").readlines()

g = []

for n in GroupsList:
    g.append(n.split(","))

#for n in g:
    #print n

def get_groupMembers(x):    #<--this method returns members from BOTH group x's
    for n in g:
        if(x in n[7]):
            print n[1] + "," + n[2]

#get_groupMembers("2")

def get_groupMembers(x,period):
    for n in g:
        if(x in n[7]):
            if(period in n[6]):
                print n[1] + "," + n[2]

#get_groupMembers("2","6")
get_groupMembers("2","7")






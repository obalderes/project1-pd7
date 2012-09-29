QuestionsList = open("questions.txt", "r").readlines()

for n in QuestionsList:
    print n

StudentsList = open("students.txt", "r").readlines()

def verifylogin(email, idnum):
    for n in StudentsList:
        if (email in n and idnum in n):
            print "true"
        else:
            print "false"
         
verifylogin("ivansmirnov13@gmail.com","8231")

def get_group(email):
    for n in StudentsList:
        if (email in n):
            print str(n)[(len(str(n))-2):]

get_group("ivansmirnov13@gmail.com")









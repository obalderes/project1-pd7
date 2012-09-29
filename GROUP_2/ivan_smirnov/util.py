QuestionsList = open("questions.txt", "r").readlines()

for n in QuestionsList:
    print n

StudentsList = open("students.txt", "r").readlines()

for n in StudentsList:
    n = str(n)

def verifylogin(idnum):
    for n in StudentsList:
        if ("idnum" in n):
            print "true"
        else:
            print "false"

         
verifylogin(8231)






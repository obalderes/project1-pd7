QuestionsList = open("questions.txt", "r").readlines()

StudentsList = open("students.txt", "r").readlines()

def verifylogin(email, idnum):    
    l = open("students.txt", "r").readlines()
    for n in l:
        if (email in n and idnum in n):
            return True
    return False

def get_group(email):
    g = open("students.txt", "r").readlines()
    for n in g:
        if (email in n):
            return str(n)[(len(str(n))-2):]


GroupsList = open("students.txt", "r").readlines()
"""<<<<<<< HEAD
g = []
=======
>>>>>>> ca2936eb94aa1ec4b125060ddb7d026f22740bc1
"""
#for n in GroupsList:
 #   g.append(n.split(","))

"""def get_groupMembers(x):    #<--this method returns members from BOTH group x's
    for n in g:
        if(x in n[7]):
            print n[1] + "," + n[2] + ";"
"""
def get_groupMembers(x,period,email):
   g = open("students.txt", "r").readlines()
   l = []
   names = []
   emails = []
   for n in g:
       l.append(n.split(','))
   for n in l:
       if(x in n[7] and period in n[6] and email not in n[0]):
           names.append(n[2])
           emails.append(n[0])
   return names,emails
   

def get_period(email):
    g = open("students.txt", "r").readlines() 
    for n in g:
        if (email in n[0]):
            return n[6]
        


#get_groupMembers("2","7","ivansmirnov13@gmail.com")



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

Grouper = open("p1.txt","r").readlines()

GroupsList = open("students.txt", "r").readlines()


def get_group_members(email):
   member_emails=[]
   members=[]
   for n in Grouper:
       if email in n:           
           member_emails = n.split(',')
   return member_emails[1:]

def get_period(email):
    g = open("students.txt", "r").readlines() 
    for n in g:
        if (email in n[0]):
            return n[6]
        


#get_groupMembers("2","7","ivansmirnov13@gmail.com")



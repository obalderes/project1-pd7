import shelve
emails = shelve.open("emails",writeback=True) #key: str(num 0-15) info: emails in lists   0-7 are groups for period 6    8-15 are groups for period 7
students = shelve.open("students",writeback=True) #key: str(emails) info: student info in dictionaries

def prepro_p1():
    f=open("p1.txt",'r')
    key=""
    for line in f.readlines():
        line = line.strip()
        e = line.partition(',')
        info = e[2].split(',')
        emails[e[0]]=info      
    f.close()

def prepro_students():
    s=open("students.txt",'r')
    key =""
    for line in s.readlines():
        line = line.strip()
        e = line.partition(',')
        info = e[2].split(',')
        students[e[0]]={"Rating Received":{},"Rating Given":{},"Last":info[0],"First":info[1],"ID":info[2],"Class":info[3],"Section":info[4],"Period":info[5],"Group":info[6],"Password":"","Project One":"",}
        group = int(float(students[e[0]]["Group"]))
        period =int(float(students[e[0]]["Period"]))
        key = str((period-6)*8+group)
        students[e[0]]["Project One"]=emails[key]
    s.close()

def printStudentsNicely():
    for key in students:
        print students[key]["First"] + ' ' + students[key]["Last"] + ": Period " + students[key]["Period"] + ", Group " + students[key]["Group"] + ", ID number: " + students[key]["ID"]

prepro_p1()
prepro_students()

def emailAuth(user,password):
    try:
        students[user]
        if(students[user]["Password"]==""):
            students[user]["Password"]=password
        elif(students[user]["Password"]!=password):
            return False
        return True
    except Exception:
        return False
'''
#rater = email string
#ratee = email string
#args can be a dictionary {"Question Number":"", "Rating":"", "Rater":"", "Ratee":""} or two string number arguments for question number and string respectively
def add_rating(rater,ratee,*args):
    #need user_authen
    if(students[rater]["Group"]==students[ratee]["Group"]):
        if(len(args)!=1): 
            rater_rating={"Question Number":args[0],"Rating":args[1],"Ratee":ratee}
            ratee_rating={"Question Number":args[0],"Rating":args[1],"Rater":rater}
        else:
            rater_rating={"Question Number":args[0]["Question Number"],"Rating":args[0]["Rating"],"Ratee":args[0]["Ratee"]}
            ratee_rating={"Question Number":args[0]["Question Number"],"Rating":args[0]["Rating"],"Rater":args[0]["Rater"]}
        students[rater]["Rating Given"].append(rater_rating)
        students[ratee]["Rating Received"].append(ratee_rating)
        return True
    else:
        return False
'''

def add_rating(rater,ratee,question,rating):
    total_question=10
    index =int(float(question[1:]))-1
    if(students[rater]["Group"]==students[ratee]["Group"]):
        if(rater not in students[ratee]["Rating Received"].keys() and ratee not in students[rater]["Rating Given"].keys()):
            students[ratee]["Rating Received"][rater]=['-1']*total_question
            students[rater]["Rating Given"][ratee]=['-1']*total_question
        students[ratee]["Rating Received"][rater][index]=rating
        students[rater]["Rating Given"][ratee][index]=rating

def userRating(user):
    dictionary={"Rating Received":students[user]["Rating Received"],"Rating Given":students[user]["Rating Given"]}
    return dictionary

def userMembers(user):
    return students[user]["Project One"]

def userFirst(user):
    name = students[user]["First"]
    return name

def userLast(user):
    name = students[user]["Last"]
    return name

def userPeriod(user):
    return students[user]["Period"]

def userGroup(user):
    return students[user]["Group"]

def userIdNumber(user):
    return students[user]["ID"]

def userClass(user):
    return students[user]["Class"]

def userSection(user):
    return students[user]["Section"]

def userInfo(user):
    dictionary={"Period":students[user]["Period"], "Group":students[user]["Group"], "Section":students[user]["Section"], "ID":students[user]["ID"], "Class":students[user]["Class"]}
    return dictionary

ratee="jdecker12@gmail.com"
rating={"Question Number":"1","Rating":"3","Rater":"mengdilin95@gmail.com","Ratee":"iBriaan@gmail.com"}
rating1={"Question Number":"1","Rating":"4","Rater":"mengdilin95@gmail.com","Ratee":"iBriaan@gmail.com"}
add_rating("mengdilin95@gmail.com",ratee,"q01","8")


print students["mengdilin95@gmail.com"]["Rating Given"]
print students[ratee]["Rating Received"]
#print get_rating("mengdilin95@gmail.com")    
   


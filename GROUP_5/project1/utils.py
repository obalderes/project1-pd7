import shelve

def prepro_p1():
    emails = shelve.open("emails",writeback=True)
    f=open("p1.txt",'r')
    key=""
    for line in f.readlines():
        line = line.strip()
        e = line.partition(',')
        info = e[2].split(',')
        emails[e[0]]=info   
    f.close()
    emails.close()
prepro_p1()

def prepro_students():
    emails = shelve.open("emails",writeback=True) 
    students = shelve.open("students",writeback=True) 
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
    emails.close()
    students.close()
prepro_students()


def printStudentsNicely():
    students = shelve.open("students",writeback=True)     
    for key in students:
        print students[key]["First"] + ' ' + students[key]["Last"] + ": Period " + students[key]["Period"] + ", Group " + students[key]["Group"] + ", ID number: " + students[key]["ID"]
    students.close()

def userAuth(user,password):
    students = shelve.open("students",writeback=True) 
    try:
        students[user]
        if(students[user]["Password"]==""):
            students[user]["Password"]=password
        elif(students[user]["Password"]!=password):
            return False
        return True
    except Exception:
        return False
    students.close()

def emailAuth(user):
    students = shelve.open("students",writeback=True) 
    try:
        students[user]
        return True
    except Exception:
        return False
    students.close()
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
#rater = email string
#ratee = email string
#question = "q01" etc
#rating = number string
def add_rating(rater,ratee,question,rating):
    students = shelve.open("students",writeback=True) 
    total_question=9
    index =int(float(question[1:]))-1
    if(students[rater]["Group"]==students[ratee]["Group"]):
        if(rater not in students[ratee]["Rating Received"].keys() and ratee not in students[rater]["Rating Given"].keys()):
            students[ratee]["Rating Received"][rater]=['-1']*total_question
            students[rater]["Rating Given"][ratee]=['-1']*total_question
        students[ratee]["Rating Received"][rater][index]=rating
        students[rater]["Rating Given"][ratee][index]=rating
        return True
    else:
        return False
    students.close()

def get_rating(user,type_rating):
    students = shelve.open("students",writeback=True) 
    d=[]
    for key in students[user][type_rating].keys():
        for index in range(len(students[user][type_rating][key])):
            if(students[user][type_rating][key][index]!='-1'):
                q='q0'+str(index+1)
                tmp=q+user+'/'+students[user][type_rating][key][index]
                d.append(tmp) #what is d?
    students.close()
    return d

def get_rating_received(user):
    type_rating="Rating Received"
    return get_rating(user,type_rating)

def get_rating_given(user):
    type_rating="Rating Given"
    return get_rating(user,type_rating)
    
def userRating(user):
    students = shelve.open("students",writeback=True) 
    dictionary={"Rating Received":students[user]["Rating Received"],"Rating Given":students[user]["Rating Given"]} #I thought it was "Ratings Recieved" and "Ratings Given" as lists of dictionaries
    students.close()
    return dictionary

def userMembers(user):
    students = shelve.open("students",writeback=True) 
    l = students[user]["Project One"]
    students.close()
    return l

def userFirst(user):
    students = shelve.open("students",writeback=True) 
    name = students[user]["First"]
    students.close()
    return name

def userLast(user):
    students = shelve.open("students",writeback=True) 
    name = students[user]["Last"]
    students.close()
    return name

def userPeriod(user):
    students = shelve.open("students",writeback=True) 
    a=students[user]["Period"]
    students.close
    return a
def userGroup(user):
    students = shelve.open("students",writeback=True) 
    a=students[user]["Group"]
    students.close()
    return a

def userIdNumber(user):
    students = shelve.open("students",writeback=True) 
    a=students[user]["ID"]
    students.close()
    return a

def userClass(user):
    students = shelve.open("students",writeback=True) 
    a=students[user]["Class"]
    students.close()
    return a

def userSection(user):
    students = shelve.open("students",writeback=True) 
    a=students[user]["Section"]
    students.close()
    return a

def userInfo(user):
    students = shelve.open("students",writeback=True) 
    dictionary={"Period":students[user]["Period"], "Group":students[user]["Group"], "Section":students[user]["Section"], "ID":students[user]["ID"], "Class":students[user]["Class"]}
    students.close()
    return dictionary
'''
if ("created" not in emails.keys()):
    prepro_p1()
if ("created" not in students.keys()):
    prepro_students()
'''
'''

ratee="jdecker12@gmail.com"
add_rating("mengdilin95@gmail.com",ratee,"q02","8")
add_rating("mengdilin95@gmail.com",ratee,"q01","9")
add_rating("mengdilin95@gmail.com",ratee,"q03","8")
add_rating("mengdilin95@gmail.com",ratee,"q04","8")
add_rating("mengdilin95@gmail.com",ratee,"q05","8")
a=[1,2,3]
a[00]=2

print students["mengdilin95@gmail.com"]["Rating Given"]
print get_rating_received(ratee)
print get_rating_given("mengdilin95@gmail.com")
#print get_rating("mengdilin95@gmail.com")    

'''
#prepro_p1()
#prepro_students()

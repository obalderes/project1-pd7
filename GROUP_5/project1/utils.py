import shelve
emails = shelve.open("emails",writeback=True) #key: str(num 0-15) info: emails in lists   0-7 are groups for period 6    8-15 are groups for period 7
students = shelve.open("students",writeback=True) #key: str(emails) info: student info in dictionaries
#raters = shelve.open("raters")
#ratees = shelve.open("ratees")

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
        students[e[0]]={"Rating Received":[],"Rating Given":[],"Last":info[0],"First":info[1],"ID":info[2],"Class":info[3],"Section":info[4],"Period":info[5],"Group":info[6],"Password":""}
    s.close()

def printStudentsNicely():
    for key in students:
        print students[key]["First"] + ' ' + students[key]["Last"] + ": Period " + students[key]["Period"] + ", Group " + students[key]["Group"] + ", ID number: " + students[key]["ID"]

'''
def raters_shelve():
    s=open("emails.txt")
    for line in s.readlines():
        line=line.strip()
        raters[line]={"Ratings":"","Project":"1","Ratees":""}
    s.close()

def ratees_shelve():
    s=open("emails.txt")
    for line in s.readlines():
        line=line.strip()
        ratees[line]={"Ratings":"","Project":"1","Raters":""}
    s.close()        
'''
prepro_p1()
prepro_students()
#raters_shelve()
#ratees_shelve()


def user_authen(user,password):
    try:
        students[user]
        if(students[user]["Password"]==""):
            students[user]["Password"]=password
        return True
    except Exception:
        return False
'''
#rater = email string
#ratee = email string
#rating = dictionary {"Question Number":"", "Rating":"", "Rater":"", "Ratee":""}
def add_rating(rater,ratee,rating):
    #needs to be wrapped around some sort of user_authen
    if(students[rater]["Group"]==students[ratee]["Group"]):
        students[rater]["Rating Given"].append(rating)
        students[ratee]["Rating Received"].append(rating)
        return True
    else:
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

def get_rating(user):
    dictionary={"Rating Received":students[user]["Rating Received"],"Rating Given":students[user]["Rating Given"]}
    return dictionary

def get_members(user):
    group = int(float(students[user]["Group"]))
    period =int(float(students[user]["Period"]))
    key = str((period-6)*8+group)
    return emails[key]

def get_name(user):
    name = students[user]["First"]+" "+students[user]["Last"]
    return name

def get_info(user):
    dictionary={"Period":students[user]["Period"], "Group":students[user]["Group"], "Section":students[user]["Section"], "ID":students[user]["ID"], "Class":students[user]["Class"]}
    return dictionary

ratee="jdecker12@gmail.com"
rating={"Question Number":"1","Rating":"3","Rater":"mengdilin95@gmail.com","Ratee":"iBriaan@gmail.com"}
rating1={"Question Number":"1","Rating":"4","Rater":"mengdilin95@gmail.com","Ratee":"iBriaan@gmail.com"}
add_rating("mengdilin95@gmail.com","iBriaan@gmail.com",rating)
add_rating("mengdilin95@gmail.com","iBriaan@gmail.com",rating1)
add_rating("mengdilin95@gmail.com",ratee,"1","8")
#print students["mengdilin95@gmail.com"]["Rating Given"]
#print students["iBriaan@gmail.com"]["Rating Received"]
#print get_rating("mengdilin95@gmail.com")    
   
u=[0]*20
print u

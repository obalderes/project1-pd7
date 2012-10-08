import shelve
emails = shelve.open("emails",writeback=True) #key: str(num 0-15) info: emails in lists   0-7 are groups for period 6    8-15 are groups for period 7
students = shelve.open("students",writeback=True) #key: str(emails) info: student info in dictionaries
#raters = shelve.open("raters")
#ratees = shelve.open("ratees")
def prepro_p1():
    f=open("p1.txt",'r')
    emailList=[]
    key=""
    for line in f.readlines():
        line= line.strip()
        if line in ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']:
            if key!="":
                emails[key]=emailList
                emailList=[]
                if len(line)>1 and line[1]!=" ":
                    key=line[0:2]
                else:
                    key= line[0] 
            elif line!=" ":
                emailList.append(line)
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
            rating={"Question Number":args[0],"Rating":args[1],"Rater":rater,"Ratee":ratee}
        else:
            rating=args[0]
        students[rater]["Rating Given"].append(rating)
        students[ratee]["Rating Received"].append(rating)
        return True
    else:
        return False

ratee="jdecker12@gmail.com"
rating={"Question Number":"1","Rating":"3","Rater":"mengdilin95@gmail.com","Ratee":"iBriaan@gmail.com"}
add_rating("mengdilin95@gmail.com","iBriaan@gmail.com",rating)
add_rating("mengdilin95@gmail.com",ratee,"1","8")

'''
def add_rating(rater,ratee,project,rating):
       return true if rating is added 
       return false if rater or ratee does not exist in the same group

def get_rating_received(user)
     return a list of ratings the user has received

def get_rating_assigned(user)
     return a list of ratings the user has given to other people





'''

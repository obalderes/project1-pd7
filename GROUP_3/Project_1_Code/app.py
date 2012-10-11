from flask import Flask
from flask import request
from flask import render_template
#import utils
from flask import url_for,redirect,flash
import databaseMethods
#import  shelveSetup

app = Flask(__name__)



@app.route("/", methods = ['GET', 'POST'])
def login():
    global email
    if request.method == "GET":

        return render_template("login.html")


    else:
        button=request.form['button'] #login button
        email = str(request.form['email'])
        assert email != ""
        if (authen(email)):
            return redirect(url_for('home'))
        else:
            return redirect(url_for('error'))

@app.route("/error", methods = ['GET', 'POST'])
def error():
 if request.method == "GET":
     return render_template("error.html")
    
@app.route("/home", methods = ['GET', 'POST'])
def home():
    global email
    
    #email = databaseMethods.getCurrentStudent()
    grades = databaseMethods.retrieveGrades(email)
    q1 = getGradeList(0, grades)
    q2 = getGradeList(1, grades)
    q3 = getGradeList(2, grades)
    q4 = getGradeList(3, grades)
    g1 = getGrades(q1)
    g2 = getGrades(q2)
    g3 = getGrades(q3)
    g4 = getGrades(q4)
    a1 = getAverage(q1)
    a2 = getAverage(q2)
    a3 = getAverage(q3)
    a4 = getAverage(q4)
    if request.method == "GET":
        name = getStudentName()
        return render_template("home.html",
                               name = name,
                               g1 = g1,
                               a1 = a1,
                               g2 = g2, 
                               a2 = a2,
                               g3 = g3, 
                               a3 = a3,
                               g4 = g4, 
                               a4 = a4)
    else:
        return redirect(url_for('rate/'))

    
#////put back in
#need to set up buttons or links to go into other group members and give ratings
#not sure what to write for displaying specific information for each user (previous ratings, fellow group members, etc.)

@app.route("/rate/", methods = ['GET', 'POST'])
def rate():
    global email
    
    #email = databaseMethods.getCurrentStudent()
    #retrieve the info of the student who logged in
  #studentInfo = databaseMethods.retrieveStudentInfo(email)
    
    #get the group number of that student
    #groupNumber = databaseMethods.getGroupNumber(email)

    #get the members of that group

    groupMembers = databaseMethods.retrieveGroupMembers(email)

    #getMyGrades(email)
    
    f = open("questions.txt", "r").readlines()
    q1 = f[0]
    q2 = f[1]
    q3 = f[2]
    q4 = f[3]
    
    p = getGroupMembers(email)
    # p1 = getGroupMembers(email, 0)
    # p2 = getGroupMembers(email, 1)
    # p3 = getGroupMembers(email, 2)
    
    p1 = p[0]
    p2 = p[1]
    p3 = p[2]


    userInfo = databaseMethods.retrieveGrades(email)
    if request.method == "GET":
        return render_template("rate.html", 
                               p1=p1,
                               p2=p2,
                               p3=p3,
                               q1=q1,
                               q2=q2,
                               q3=q3,
                               q4=q4)
    else:
        x = 0
        s = databaseMethods.retrieveGroupMembers(email)
        e1 = ""
        e2 = ""
        e3 = ""
        for each in range(0,4):
            if s[each] == email:
                pass
        else:
                if e1 == "":
                    e1 = s[each]
                else:
                    if e2 == "":
                        e2 = s[each]
                    else:
                        e3 = s[each]
        
               
           
        button=request.form['button'] 
        m1 = {request.form['p1q1'], request.form['p1q2'], request.form['p1q3'], request.form['p1q4']}
        m2 = {request.form['p1q1'], request.form['p1q2'], request.form['p1q3'], request.form['p1q4']}
        m3 = {request.form['p1q1'], request.form['p1q2'], request.form['p1q3'], request.form['p1q4']}
        databaseMethods.setGrades(m1 , e1)
        databaseMethods.setGrades(m2, e2)
        databaseMethods.setGrades(m3, e3)
           
           #except:
               





def getGradeList( i, grades ):
    if len(grades) != 0:
        return grades[i]
    else:
        return 0


def getStudentName():
    global email
    #email = databaseMethods.getCurrentStudent()
    info = databaseMethods.retrieveStudentInfo(email)
    name = info[1] + " " + info[0]
    return name

def getAverage(question):
    if len(question) == 0:
        return "No grades"
    ans = 0
    total = 0
    count = 0
    for count in question:
        ans = question[count]
        total = total + 1

    return ans/total

def getGrades(question):
    if len(question) == 0:
        return "No grades"
    ans = ""
    count = 0
    for count in question:
               ans = ans + str(question[count]) + ", "
    return ans

def getGroupMembers(email):
    s = databaseMethods.retrieveGroupMembers(email)
    ans = []
    for each in range(0,4):
        if s[each] == email:
            pass
        else:
            info = databaseMethods.retrieveStudentInfo(s[each])
            name = info[1] + " " + info[0]
            ans.append(name)
    return ans

def authen(email):
    return databaseMethods.isAKey(email)

    
if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run(port = 7003) 



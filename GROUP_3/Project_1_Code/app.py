from flask import Flask
from flask import request
from flask import render_template
#import utils
from flask import url_for,redirect,flash
import databaseMethods
#import  shelveSetup

app = Flask(__name__)



#shelveSetup.getStudentInfo()
#shelveSetup.getGroups()
#shelveSetup.setupGrades()
#shelveSetup.setupRatedBy()


@app.route("/", methods = ['GET', 'POST'])
def login():
    global email
    if request.method == "GET":

        return render_template("login.html")


    else:
        button=request.form['button'] #login button
        email = str(request.form['email'])
        assert email != ""
        #databaseMethods.saveCurrentStudent(email) 
        return redirect(url_for('home'))
 

    
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

@app.route("/rate/")
def rate():
    global email
    #email = databaseMethods.getCurrentStudent()
    #retrieve the info of the student who logged in
    studentInfo = databaseMethods.retrieveStudentInfo(email)
    
    #get the group number of that student
    groupNumber = databaseMethods.getGroupNumber(email)

    #get the members of that group
    groupMembers = retrieveGroupMembers(groupNumber)

    #getMyGrades(email)
    userInfo = databaseMethods.retrieveGrades(email)
    return render_template("rate.html")


def getGradeList( i, grades ):
    if len(grades) != 0:
        return grades[i]

def getStudentName():
    global email
    #email = databaseMethods.getCurrentStudent()
    info = databaseMethods.retrieveStudentInfo(email)
    name = info[1] + " " + info[0]
    return name

def getAverage(question):
    ans = 0
    total = 0
    count = 0
    for count in question:
        ans = question[count]
        total = total + 1

    return ans/total

def getGrades(question):
    ans = ""
    count = 0
    for count in question:
        ans = ans + str(question[count]) + ", "
    return ans

    

if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run() 



from flask import Flask
from flask import request
from flask import render_template
#import utils
from flask import url_for,redirect,flash
import databaseMethods, shelveSetup

app = Flask(__name__)



#shelveSetup.getStudentInfo()
#shelveSetup.getGroups()
#shelveSetup.setupGrades()
#shelveSetup.setupRatedBy()


@app.route("/", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":

        return render_template("login.html")


    else:
        button=request.form['button'] #login button
        return redirect(url_for('home')) 
#needs to do authentication before directing to login. could be ID
    email = request.form['email']
    assert email != ""
    databaseMethods.saveCurrentStudent(email) 
 


@app.route("/home", methods = ['GET', 'POST'])
def home():
    grades = retrieveGrades(email)
    q1 = getGradeList(0, grades)
    q2 = getGradeList(1, grades)
    q3 = getGradeList(2, grades)
    q4 = getGradeList(3, grades)
    if request.method == "GET":
        return render_template("home.html", 
                               q1 = q1, 
                               q2 = q2, 
                               q3 = q3, 
                               q4 = q4)
    else:
        return redirect(url_for('rate/'))

    grades = databaseMethods.retrieve
    
#////put back in
#need to set up buttons or links to go into other group members and give ratings
#not sure what to write for displaying specific information for each user (previous ratings, fellow group members, etc.)

@app.route("/rate/")
def rate():

    email = databaseMethods.getCurrentStudent()

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
    return grades[i]


if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run() 



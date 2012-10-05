from flask import Flask
from flask import request
from flask import render_template
import utils
from flask import url_for,redirect,flash


app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("homepage.html")
    else:
        button=request.homepage['button'] #login button
        return redirect(url_for('login')) #needs to do authentication before directing to login. could be ID
    email = request.homepage['email'] 
    assert name != ""
    databaseMethods.retrieveStudentInfo(email)
    #groupNumber = databaseMethods.getGroupNumber(email) <-- DENIS MAKE THIS
    retrieveGroupMembers(groupNumber)
    #getMyGrades(email) <--DENIS MAKE THIS
    #userInfo = databaseMethods.get_User() <-- should access first shelve DENIS made. 
    
    
    
    #flash?


@app.route("/login", methods = ['GET', 'POST']
#I THINK WE NEED get and post yet again b/c we want to have inputs on this page as well. 
def login():
    
     return render_template("loginPage.html")
#info about ratings and buttons that lead to new pages to 
button = request.loginPage['button'] #need to set up buttons or links to go into other group members and give ratings
#not sure what to write for displaying specific information for each user (previous ratings, fellow group members, etc.)

@app.route("/rate")
def rate():
    return render_template("rate.html")

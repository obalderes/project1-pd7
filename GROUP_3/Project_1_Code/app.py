from flask import Flask
from flask import request
from flask import render_template
#import utils
from flask import url_for,redirect,flash
import databaseMethods

app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("login.html")
    else:
        button=request.form['button'] #login button
       # return redirect(url_for('home')) #needs to do authentication before directing to login. could be ID
    email = request.form['email']
    assert email != ""
    databaseMethods.retrieveStudentInfo(email)
    #groupNumber = databaseMethods.getGroupNumber(email) <-- DENIS MAKE THIS
    retrieveGroupMembers(groupNumber)
    #getMyGrades(email) <--DENIS MAKE THIS
    #userInfo = databaseMethods.get_User() <-- should access first shelve DENIS made.
   
   
   
    #flash?

#I THINK WE NEED get and post yet again b/c we want to have inputs on this page as well.
@app.route("/home", methods = ['GET', 'POST'])
def login():
   if request.method == "GET":
       return render_template("home.html")
#info about ratings and buttons that lead to new pages to
#////Put back in
   else: 
       button = request.loginPage['button'] 
    
#////put back in
#need to set up buttons or links to go into other group members and give ratings
#not sure what to write for displaying specific information for each user (previous ratings, fellow group members, etc.)

@app.route("/rate")
def rate():
    return render_template("rate.html")

if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run() 

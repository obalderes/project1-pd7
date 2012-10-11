from flask import Flask
from flask import url_for, redirect, request, render_template
import utils

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])


#failedpass will check to see if the user had already tried to log in.
#if he has, it will display a message telling him that he or she provided
#an invalid email address.
#-Brian Lam
def index(failedpass = False):
    if request.method=="GET":
        return render_template("index.html")
    if failedpass == True:
        return render_template("index.html", failedpass = True)
    elif request.method=="POST":
        email = request.form['email']
        assert email != ""
        return login(email)

useremail = ""

#Takes an email address and checks to see if it's in the email list.
#If it fails the authentification, the website will display a
#message in red.
#-Brian Lam
def login(email):
    email = str(email)
    if(utils.emailAuth(email) == True):
        print email + " Passed auth"
        fullname = utils.userFirst(email) + " " + utils.userLast(email)
        global useremail
        useremail = email
        return rate(email, fullname)
        
    else:
        print email + " Failed auth"
        failedpass = True
        return index(failedpass = True)
    
@app.route("/rate")
@app.route("/rate/<name>", methods = ['GET', 'POST'])
#Rate v2, maybe rewriting the code will fix our error?
def rate(email, name):
    members = utils.userGroupMembers(email)
    ratings = utils.get_response(email)
    return render_template("rate.html", name = name, members = members, ratings=ratings)
    if (request.form(buttonvalue == "Submit")):
        return confirm()
    
@app.route("/viewratings")
def viewratings(email):
    ratings = utils.get_ratings(email,"Rating Recieved")
    return render_template("viewratings.html", ratings=ratings)
#Coded by Brian Lam
#Many thanks to Bernie Birnbaum for catching what was wrong with my Submit button
#for two days
@app.route("/confirm", methods = ['GET', 'POST'])
def confirm():
    l = []
    members = utils.userGroupMembers(useremail)
    for member in members:
        l.append(str("q1"+member+":")+str(request.form["q1"+member]))
        l.append(str("q2"+member+":")+str(request.form["q2"+member]))
        l.append(str("q3"+member+":")+str(request.form["q3"+member]))
        l.append(str("q4"+member+":")+str(request.form["q4"+member]))
        l.append(str("q5"+member+":")+str(request.form["q5"+member]))
<<<<<<< HEAD
        print l
        utils.save_response(useremail,l)
    return render_template("confirm.html")
=======
    print l
    utils.save_response(useremail,l)
    ratings = utils.get_ownratings(useremail)
    return render_template("confirm.html", ratings=ratings)
>>>>>>> 392ca070469e442a8022851ab02abde036a38d7a

if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask, render_template, request
import database
import shelve
import sys
import stat

app = Flask(__name__)
globalemail = ""

@app.route("/", methods = ["GET", "POST"])
def home():
    global globalemail
    """
    On the main page a user will type in their email and press the login button.
    This will lead them to a second page (choice.html).
    """
    error = ""
    if request.method == "POST":
        if valid_login(request.form['email'], request.form['IDnum']):
            globalemail = str(request.form['email'])
            return log_the_user_in()
        else:
            error = "Invalid username/password"

    return render_template("login.html", error=error)

@app.route("/choose/", methods = ["GET", "POST"])
def log_the_user_in():
    global globalemail
    """
    The user arrives at this page if they login successfully.
    Here, they can choose whether they want to a) see ratings or b) rate people.
    """
        
    return render_template("page.html")

@app.route("/rate/", methods = ["GET", "POST"])
def rate_page():
    return render_template("rate.html")

@app.route("/ratings/", methods = ["GET", "POST"])
def ratings_page():
    global globalemail
    """
    I don't really feel like doing the thing Z talked about in class for this so I'll just hardcode stuff. Might do some fancy visualization stuff with d3.js if I have time and feel like it- this is pretty barebones.
    """
    f = open("questions.txt", "r").readlines()

    q1ans = ""
    q2ans = ""
    q3ans = ""
    q4ans = ""
    for rating in database.getRatings(globalemail):
        q1ans += str(rating[0]) + " "
        q2ans += str(rating[1]) + " "
        q3ans += str(rating[2]) + " "
        q4ans += str(rating[3]) + " "
    
    return render_template("ratings.html",
                           q1=f[0],
                           q1ans=q1ans,
                           q2=f[1],
                           q2ans=q2ans,
                           q3=f[2],
                           q3ans=q3ans,
                           q4=f[3],
                           q4ans=q4ans)

def valid_login(email, IDnum):
    auth = shelve.open("authen")
    valid = False
    try:
        valid = auth[str(email)][2] == IDnum
    except KeyError, e:
        return valid
    else:
        return valid

if __name__ == "__main__":
    app.run(debug=True)

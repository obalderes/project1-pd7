from flask import Flask, render_template, request
import database
import shelve
import sys
import stat

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():
    """
    On the main page a user will type in their email and press the login button.
    This will lead them to a second page (choice.html).
    """
    error = ""
    if request.method == "POST":
        if valid_login(request.form['email'], request.form['IDnum']):
            return log_the_user_in(request.form['email'])
        else:
            error = "Invalid username/password"
            

    return render_template("login.html", error=error)

@app.route("/choose/", methods = ["GET", "POST"])
def log_the_user_in(email):
    """
    The user arrives at this page if they login successfully.
    Here, they can choose whether they want to a) see ratings or b) rate people.
    """
        
    return render_template("choice.html")

@app.route("/rate/", methods = ["GET", "POST"])
def rate_page():
    return render_template("rate.html")

@app.route("/ratings/", methods = ["GET", "POST"])
def ratings_page():
    return render_template("ratings.html")
    

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

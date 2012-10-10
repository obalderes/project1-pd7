from flask import Flask
from flask import url_for, redirect, request, render_template
import shelve
import utils

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index(failedpass = False):
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        button = request.form['button']
        email = request.form['email']
        assert email != ""
        return login(email)

def login(email):
    email = str(email)
    if(utils.emailAuth(email) == True):
        print email + " Passed auth"
        fullname = utils.userFirst(email) + " " + utils.userLast(email)
        return rate(email, fullname)
    else:
        print email + " Failed auth"
        return redirect(url_for("index", failedpass = True))
    
@app.route("/rate")
@app.route("/rate/<name>", methods = ['GET', 'POST'])
def rate(email = "", name = "Stranger", rated = "false"):
    if request.method=="POST":
        members = utils.userMembers(email)
        return render_template("rate.html", name = name, members = members)
        submit = request.form["Submit"]
        if submit == "Submit":
            return confirm()
    if request.method=="POST":
        members = utils.userMembers(email)
        return render_template("rate.html", name = name, members = members)
        submit = request.form["Submit"]
        if submit == "Submit":
            return confirm()

@app.route("/confirm")
def confirm():
    return render_template("confirm.html")

if __name__ == "__main__":
    app.run(debug=True)

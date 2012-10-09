from flask import Flask
from flask import url_for, redirect, request, render_template
import utils

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index(failedpass = False):
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        button = request.form['button']
        email = request.form['email']
        #password = request.form['password']
        assert email != ""
        return login(email)

def login(email):
    email = str(email)
    if(utils.emailAuth(email) == True):
        print email + " Passed auth"
        fullname = utils.userFirst(email) + " " + utils.userLast(email)
        #members = utils.userGroupMembers("iBriaan@gmail.com")
        return redirect(url_for("rate", members = utils.userGroupMembers(email), email=email, name = utils.userFirst(email)))
    else:
        print email + " Failed auth"
        return redirect(url_for("index", failedpass = True))
    
@app.route("/rate")
@app.route("/rate/<name>", methods = ['GET', 'POST'])
def rate(email = "", name = "Stranger"):
    members = utils.userGroupMembers("iBriaan@gmail.com")
    return render_template("rate.html", name = name, members = members)

if __name__ == "__main__":
    app.run(debug=True)

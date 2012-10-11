from flask import Flask
from flask import url_for, redirect, request, render_template
import utils

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index(failedpass = False):
    if request.method=="GET":
        return render_template("index.html")
    if failedpass == True:
        return render_template("index.html", failedpass = True)
    elif request.method=="POST":
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
        failedpass = True
        return index(failedpass = True)
    
@app.route("/rate")
@app.route("/rate/<name>", methods = ['GET', 'POST'])
def rate(email = "", name = "Stranger"):
    try:
        members = utils.userGroupMembers(email)
        return render_template("rate.html", name = name, members = members)
    except Exception:
        Exception.printStackTrace()
    #Still don't understand why this code won't work. It's linked
    #in with the issue to the Submit button producing an error. Aagghhhhh
    #EDIT: Changed some stuff, now it doesn't produce an error, it just
    #goes back to the homepage
    #-Brian Lam
    buttonvalue = str(request.form['button'])
    if (buttonvalue == "Submit"):
        return confirm()
        """
    assert request.form["button"] != ""
    if (request.form["button"] == ""):
        print "Error: empty"
    else:
        print request.form["button"]
    if request.method == "POST":
        return confirm()
    """

@app.route("/confirm")
def confirm():
    return render_template("confirm.html")

if __name__ == "__main__":
    app.run(debug=True)

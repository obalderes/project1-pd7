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
        password = request.form['password']
        assert email != ""
        return login(email,password)

def login(email, password):
    if(utils.user_authen(email) == True):
        return redirect(url_for("rate", name = email))
    else:
        return redirect(url_for("index", failedpass = True))
    
@app.route("/rate")
@app.route("/rate/<name>", methods = ['GET', 'POST'])
def rate(name = "Stranger"):
    return render_template("rate.html", name = name)

if __name__ == "__main__":
    app.run(debug=True)

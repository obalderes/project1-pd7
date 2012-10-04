from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

"""
@app.route(pathway)
This defines the URL that will call the function after it.
By default, a route only answers to HTTP GET requests.
That can be changed by providing the 'methods' argument to the route() decorator.
"""
@app.route("/", methods = ["GET", "POST"])
def home():
    #renders the homepage template
    return render_template("page.html")



#This is not the way we want to do it in the end, it's just a proof of concept
@app.route("/login/", methods = ["GET", "POST"])
def login():
    error = ""
    if request.method == "POST":
        if valid_login(request.form['email'], request.form['IDnum']):
            return log_the_user_in(request.form['email'])
        else:
            error = "Invalid username/password"
            print error
    return render_template("login.html", error=error)


@app.route("/choice/", methods = ["GET", "POST"])
def choice():
    return render_template("page.html")

def valid_login(email, IDnum):
    return email.find("@") != -1

def log_the_user_in(email):
    return render_template("hello.html")

if __name__ == "__main__":
    app.run(debug=True)


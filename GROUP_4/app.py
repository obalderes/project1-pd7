from flask import Flask, render_template, request
import database
import shelve

app = Flask(__name__)

"""
@app.route(pathway)
This defines the URL that will call the function after it.
By default, a route only answers to HTTP get requests.
That can be changed by providing the 'methods' argument to the route() decorator.
"""
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

    return render_template("login.html")

@app.route("/choose/", methods = ["GET", "POST"])
def log_the_user_in(email):
    """
    The user arrives at this page if they login successfully.
    Here, they can choose whether they want to a) see ratings or b) rate people.
    """
        
    return render_template("choice.html")

def valid_login(email, IDnum):
    auth = shelve.open("authen")
    return auth[str(email)][2] == IDnum

if __name__ == "__main__":
    app.run(debug=True)

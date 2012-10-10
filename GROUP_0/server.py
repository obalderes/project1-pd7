from flask import Flask, request, render_template, url_for, redirect, flash
import database

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        session['username'] = request.home["username"]
        if not(database.isUsername(session['username'])):
            flash("%s is not an authorized email. \nPlease enter a valid username."%(session['username']))
            return redirect(url_for("home"))
        #check if valid username. If not, error message.
        session['information'] = database.getInformation(session['username'])
        button = request.home["button"]
        if button == "View Ratings":
            return redirect(url_for("view_ratings"))
        elif button == "Post Ratings":
            return redirect(url_for("post_ratings"))
        
@app.route("/view_ratings", methods = ['GET','POST'])
def view_ratings():
    if session['username'] == "":
        flash("Please enter a username on the home page.")
        return redirect(url_for("home"))
    if request.method == "GET":
        return render_template("view_ratings.html", username = session['username'], information = session)
    else:
        button = request.view_ratings["button"]
        if button == "Home":
            return redirect(url_for("home"))
        elif button == "Post Ratings":
            return redirect(url_for("post_ratings"))

@app.route("/post_ratings", methods = ['GET', 'POST'])
def post_ratings():
    if session['username'] == "":
        flash("Please enter a username on the home page.")
        return redirect(url_for("home"))
    if request.method == "GET":
        name = database.getName(session['username'])
        return render_template("post_ratings", username = session['username'], username.first = name[0], username.last = name[1], listofratees = database.getRatees(session['username']))
    
if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run() # connect to localhost:5000 or http://127.0.0.1:5000
        

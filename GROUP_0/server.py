import flask
from flask import *
import database

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        session['username'] = request.form["username"]
       #check if valid username. If not, error message.
        if not(database.isUsername(session['username'])):
            flash("%s is not an authorized email. \nPlease enter a valid username."%(session['username']))
            session['username'] = ""
            return redirect(url_for("home"))
        button = request.form["button"]
        if button == "View Ratings":
            return redirect(url_for("view_ratings"))
        elif button == "Post Ratings":
            return redirect(url_for("post_ratings"))
        
@app.route("/view_ratings", methods = ['GET','POST'])
def view_ratings():
    if session['username'] == "":
        flash("Please enter a valid username on the home page.")
        return redirect(url_for("home"))
    if request.method == "GET":
        user = session['username']
        name = database.getName(user)
        questions = open("questions.txt", "r").readlines()
        return render_template("view_ratings.html", username = user, first = name[0], last = name[1], ratings = database.getRatings(user), questions = questions)
    else:
        button = request.form["button"]
        if button == "Cancel":
            session['username'] = ""
            return redirect(url_for("home"))
        elif button == "Post Ratings":
            return redirect(url_for("post_ratings"))

@app.route("/post_ratings", methods = ['GET', 'POST'])
def post_ratings():
    if session['username'] == "":
        flash("Please enter a valid username on the home page.")
        return redirect(url_for("home"))
    user = session['username']
    name = database.getName(user)
    questions = open("questions.txt", "r").readlines()
    ratees = database.getRatees(user)
    project = database.getCurrentProject(user)
    if request.method == "GET":
        return render_template("post_ratings.html", username = user, first = name[0], last = name[1], ratees = ratees, project = project, questions = questions)
    else:
        button = request.form["button"]
        if button == "Cancel":
            session['username'] == ""
            return redirect(url_for("home"))
        elif button == "Save":
            ratings = {}
            for groupmember in ratees:
                ratings[groupmember] = {}
                for qnum in range(len(questions)):
                    ratings[groupmember[qnum]] = []
                    for n in range(10):
                        if request.form["%i:%s:%i:%i"%(project, groupmember, qnum, n)] == 'CHECKED':
                            ratings[groupmember[qnum]] += n
            database.setRatings(ratings)
            session['username'] = ""
            return redirect(url_for("home"))
                        
                
            
        
    
if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run() # connect to localhost:5000 or http://127.0.0.1:5000
        

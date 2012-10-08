import Flask
import database

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        username = request.home["username"]
        if !(database.isUsername(username)):
            flash("%s is not an authorized email. \nPlease enter a valid username."%(username))
            return redirect(url_for("home"))
        #check if valid username. If not, error message.
        button = request.home["button"]
        if button == "View Ratings":
            return redirect(url_for("view_ratings", username = username))
        elif button == "Post Ratings":
            return redirect(url_for("post_ratings", username = username))
        #redirect to page corresponding to button value

@app.route("/view_ratings", methods = ['GET','POST'])
def view_ratings():
    if request.method == "GET":
        return render_template("view_ratings.html")
    else:
        button = request.view_ratings["button"]
        if button == "Home":
            return redirect(url_for("home"))
        elif button == "Post Ratings":
            return redirect(url_for("post_ratings"))

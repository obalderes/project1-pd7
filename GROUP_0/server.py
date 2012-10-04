import Flask
import database

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        username = request.form["username"]
        #WHAT IS THE NAME OF THE BELOW METHOD
        if !(database.isUsername(username)):
            flash("%s is not an authorized email. \nplease enter a valid username."%(username))
            return redirect(url_for("home"))
        button = request.form["button"]
        if button == "

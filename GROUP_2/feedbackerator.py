from flask import Flask
from flask import request, render_template, url_for, redirect, flash

app = Flask(__name__)
app.secret_key = 'Whatever'

qlist = ["How awesome are they?", "How compliant?", "How knowledgable", "How much effort?", "How much of a team player?"]

@app.route("/", methods = ['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        button = request.form['button']
        username = request.form['username']
        assert username != ""
        flash("User " + username)
        return redirect(url_for('home', name = username))

@app.route("/home", name = None)
@app.route("/home/<name>", methods = ['GET', 'POST'])
def user_page():
    if name == None:
        return redirect(url_for(''))
    if request.method == "GET":
        return render_template("user_page.html")

@app.route("/rate", methods = ['GET', 'POST'])
def rate_page():
    if request.method == "GET":
        return render_template("rate_page.html",qlist=qlist)
    else:
        button = request.form['button']
    
    name = request.form['student_rated']
    rating = request.form['rating']
    assert name != ""

def view_results():
    if request.method == "GET":
        return render_template("results.html")
    else:
        button = request.form['button']
    
    name=request.form['student_rated']
    rating = request.form['rating']
    assert name != ""
    flash("Name:%s Rating:%s"%(name,rating))
                        

if __name__ == "__main__":
    app.debug = True
    app.run()

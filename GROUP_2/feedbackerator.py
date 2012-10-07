from flask import Flask
import util2
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
        password = request.form['password']
        assert username != ""
        assert password != ""
        #flash("User " + username)
        return redirect(url_for('user_page', name = username)) #So frustrated. This is an important note to self, David. When you use url_for, the String input is the name of the method of the page, not it's actual URL. Agh!

@app.route("/home")
@app.route("/home/<name>", methods = ['GET', 'POST'])
def user_page(name=None):
    if name == None:
        return redirect(url_for('login'))
    
    if request.method == "GET":
        return render_template("user_page.html", name=name)
    else:
        button = request.form['button']
        if button == 'Rate':
            return redirect(url_for('rate_page'))
        elif button == 'View':
            return redirect(url_for('view_results'))


@app.route("/rate", methods = ['GET', 'POST'])
def rate_page():
    if request.method == "GET":
        return render_template("rate_page.html",qlist=qlist)
    else:
        button = request.form['button']
    
    name = request.form['student_rated']
    rating = request.form['rating']
    assert name != ""

@app.route("/results")
def view_results():
   
    return render_template("results.html")


if __name__ == "__main__":
    app.debug = True
    app.run()

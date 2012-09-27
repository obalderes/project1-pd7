from flask import Flask
from flask import render_template
from flask import request, url_for, redirect, flash

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    
    if request.method == "GET":
        return render_template("t1.html")
    
    else:
        username = request.form['username']
        button = request.form['button']
        assert username != ""
        return redirect(url_for('login',name = username))

@app.route("/login")
@app.route("/login/<name>")
def login(name = None):
    return render_template("t2.html", name = name)

        


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import request
from flask import render_template
import utils
from flask import url_for,redirect,flash


app = Flask(__name__)


@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("homepage.html")
    else:
        button=request.homepage['button']
        return redirect(url_for('login'))
    name = request.homepage['email']
    assert name != ""
    utils.save_email(name)
    #flash?


@app.route("/login")
def login():
    userInfo = utils.get_User()
#should use email from login on homepage to fill in multi dimensional array
#with user info
     return render_template("loginPage.html")
info about ratings and buttons that lead to new pages to 
button = request.loginPage['button']



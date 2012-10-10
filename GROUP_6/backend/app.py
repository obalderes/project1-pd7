import storage
import shelve
import os
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash
app = Flask(__name__)
app.secret_key = 'some_secret'
Email=""
@app.route("/",methods = ['get','post'])
def login():
    if request.method=='GET':
        return render_template("homepage.html")
    else:
        Email=request.form['username']
        button = request.form['button']
        if button == 'Login':
            if storage.checkUser(Email):
                return redirect(url_for("rate"))
            else:
                return redirect(url_for(""))
        else:
            return redirect(url_for("page_not_found"))


@app.route('/fail')
def page_not_found():
    abort(404)

@app.route('/Rater',methods=['get','post'])
def rate():
    if request.method=='GET':
        return render_template("RatingPage.html",username = Email)
    else:
        return redirect(url_for(""))
   
    
if __name__=="__main__":
    app.debug=True
    app.run()

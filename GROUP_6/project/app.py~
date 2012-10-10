import storage
import shelve
import os
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash,session
app = Flask(__name__)
app.secret_key = 'some_secret'
Email=""
IDList = []
@app.route("/",methods = ['get','post'])
def login():
    if request.method=='GET':
        return render_template("homepage.html")
    else:

        button = request.form['button']
        if button == 'Rate':
            Email = str(request.form["username"])
            if storage.checkUser(Email)==True:
                return redirect(url_for("rate"))
            else:
                return redirect(url_for("page_not_found"))
        else:
            return redirect(url_for("page_not_found"))


@app.route('/fail')
def page_not_found():
    return render_template("Fail.html")

@app.route('/Rater',methods=['get'])
def rate():
    if request.method=='GET':
        return render_template('RatingPage.html', Email = Email)
    else:
        return redirect(url_for('login'))
   
'''
def getRatings(email):
    return storage.s['id',email]

def rate(email,r1,r2,r3,comment):
    storage.s['responses',email,1] = r1
    storage.s['responses',email,2] = r2
    storage.s['responses',email,3] = r3
    storage.s['responses',email,4] = comment

def getInfo(email):
    namesList =[]
    namesList[1] = storage.s[email,firstName]
    namesList.append(storage.s[email,lastName])
'''
    
if __name__=="__main__":
    app.debug=True
    app.run()

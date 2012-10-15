import storage
import shelve
import os
from flask import Flask
from flask import request
from flask import render_template
from flask import url_for,redirect,flash,session
app = Flask(__name__)
app.secret_key = 'some_secret'


@app.route("/",methods = ['get','post'])
def login():
    global groupsize
    global currentCounter
    global MembersofGroup
    global email
    global IDList
    if request.method=='GET':
        return render_template("homepage.html")
    else:

        button = request.form['button']
        if button == 'Rate':
            print "HI"
            email = request.form["username"]
            if storage.checkUser(email)==True:
                IDList = storage.getInfo(email)
                MembersofGroup = storage.returnGroupList(email)
                groupsize = len(MembersofGroup)
                currentCounter = 0
                return redirect(url_for("rate"))
            else:
                return redirect(url_for("page_not_found"))
        elif button == 'Get Ratings!':
            email = request.form["username"]
            if storage.checkUser(email)==True:
                IDList = storage.getInfo(email)
                MembersofGroup = storage.returnGroupList(email)
                currentCounter = 0
                return redirect(url_for("viewRates"))
            else:
                return redirect(url_for("page_not_found"))
        else:
            return redirect(url_for("page_not_found"))

@app.route('/fail')
def page_not_found():
    global currentCounter
    global MembersofGroup
    global email
    global IDList
    return render_template("Fail.html")

@app.route('/view')
def viewRates():
    global currentCounter
    global MembersofGroup
    global email
    global IDList
    return render_template("ViewRatings.html",info=IDList)

@app.route('/Rater',methods=['GET','POST'])
def rate():
    global email
    global IDList
    global MembersofGroup
    global currentCounter
    global groupsize
    if request.method == 'GET':   
        return render_template('RatingPage.html',currentRatee =storage.getInfo( MembersofGroup[currentCounter])[0])
    else:
        if request.form["button"] == "Rate":

                r1 = str(request.form["rating1"])
                r2 = str(request.form["rating2"])
                r3 = str(request.form["rating3"])
                r4 = str(request.form["rating4"])
                comment = str(request.form["comment"])
                storage.addRating(email,storage.getInfo( MembersofGroup[currentCounter])[0],r1,r2,r3,r4,comment)
                currentCounter = currentCounter+1
                if currentCounter < groupsize:
                    return redirect(url_for('rate',currentRatee =storage.getInfo( MembersofGroup[currentCounter])[0]))

                else:
                    return redirect(url_for('Success'))

@app.route("/Success")
def Success():
    return render_template("Success.html")

if __name__=="__main__":
    app.debug=True
    app.run()

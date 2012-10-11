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
    global currentCounter
    global MembersofGroup
    global email
    global IDList
    if request.method=='GET':
        return render_template("homepage.html")
    else:

        button = request.form['button']
        if button == 'Rate':
            email = request.form["username"]
            if storage.checkUser(email)==True:
                IDList = storage.getInfo(email)
                MembersofGroup = storage.returnGroupList(email)
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

@app.route('/Rater',methods=['get'])
def rate():
    global email
    global IDList
    global MembersofGroup
    global currentCounter
    if request.method=='GET':   
        print MembersofGroup
        return render_template('RatingPage.html',currentRatee =storage.getInfo( MembersofGroup[currentCounter])[0])
    elif request.form('button') == "Rate!":
        counter = (counter + 1)
        if counter == (len(MembersofGroup)):
            r1 = str(request.form["rating1"])
            r2 = str(request.form["rating2"])
            r3 = str(request.form["rating3"])
            r4 = str(request.form["rating4"])
            comment = str(request.form["comment"])
            storage.addRating(email,MembersofGroup[currentCounter],r1,r2,r3,r4,comment)
            return redirect(url_for('Success'))
        else:
            r1 = str(request.form["rating1"])
            r2 = str(request.form["rating2"])
            r3 = str(request.form["rating3"])
            r4 = str(request.form["rating4"])
            comment = str(request.form["comment"])
            storage.addRating(email,MembersofGroup[currentCounter],r1,r2,r3,r4,comment)
            return render_template('RatingPage.html')
            
    else:
        return redirect(url_for('login'))
@app.route("/Success")
def Success():
    return render_template("Success.html")
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

from flask import Flask
from flask import request
from flask import render_template
import utils
import math
from flask import url_for,redirect,flash

app = Flask(__name__)
app.secret_key = 'some_secret'

#loggedin = True
#email = 'iouthwaite1@gmail.com'

@app.route("/")
def home():
   loggedin = True
   email = 'iouthwaite1@gmail.com'
   if loggedin==False:
        email=request.form["username"]
        paswrd=request.form["idnum"]
        if (database.getuser):
            loggedin = true
        #return render_template("index.html", loggedin=loggedin)
   else:
        info = datastorage.getData(email)
        projects = []
        count = 1
        while(count <= len(info)):
            projects.append(('project' + count)[])
            count = count + 1

        numratings = 0
        sumratings = 0
        scores = []
        for projs in info:
            for ratings in info[projs]:
                numratings = numratings + 1
                sumratings = sumratings + info[projs][ratings]['score']
                scores.append(info[projs][ratings]['score'])
        avgrating = sumratings / numratings
        ex = 0
        for score in scores:
            ex = ex + (scores[score]-avgrating) * (scores[score]-avgrating)
        stdev = sqrt(ex/numratings)
        
        # I need to get first and last names and groupmembers from databases and we need 
        #need a questions file.



        datastorage.ratePerson(email, emailratee, question, score, comments)

        print avgscore
        print stdev
                              
        
                
                
        


if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run() # connect to localhost:5000 or http://127.0.0.1:5000

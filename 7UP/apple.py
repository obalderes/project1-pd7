from flask import Flask, request, render_template
import datastorage
import math
from flask import session,url_for,redirect,flash

app = Flask(__name__)
app.secret_key = 'some_secret'

global questions
global email
global loggedin

q = open('question.txt')

@app.route("/",methods=['GET','POST'])
def home():
   if email in session:
      return redirect(url_for('/rate'))
   else:
      return redirect(url_for('/login'))
        
@app.route('/login', methods=['GET','POST'])
def login():
   if request.method == 'POST':
        email = request.form["username"]
        paswrd = request.form["idnum"]
        if datastorage.isUser(email):
           loggedin = True
           session[email]=True
           return redirect(url_for('home'))
   return render_template('index.html',loggedin=False,projects=None,questions=q,avgrating=None,stdex=None,questionavgs=None)

@app.route('/logout')
def logout():
   session.pop(email, None)
   return redirect(url_for('home'))        

        
@app.route('/rate', methods=['GET','POST'])
def rate():
   if email in session:
      if request.method=='POST':
         rater = email
         rating1 = request.form('question1')
         rating2 = request.form('question2')
         rating3 = request.form('question3')
         ratee = request.form('ratees')
         datastorage.ratePerson(rater=rater, ratee=ratee,question=questions[1],score=rating1,comments=None)
         datastorage.ratePerson(rater=rater, ratee=ratee,question=questions[2],score=rating2,comments=None)

         datastorage.ratePerson(rater=rater, ratee=ratee,question=questions[3],score=rating2,comments=None)
         info = datastorage.getData(email)
         projects = []
         count = 1
         while(count <= len(info)):
            projects.append(datastorage.getGroupMembers(email,count))
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

         first = datastorage.getFirst(email)
         last = datastorage.getLast(email)

         questions=['how smart was your groupmate', 'how much did they help', 'blah,blah, blah']



         questionavgs=[]
         for x in range(len(questions)):
           r=0
           for i in range(len(info)):
              r=r+datastorage.getAvgForQuestion(email,i+1,questions[x])
           questionavgs.append(r/len(info))



      return render_template('index.html',loggedin=True,projects=projects,questions=questions,\
avgrating=avgrating,stdex=stdev,questionavgs=questionavgs)




if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run() # connect to localhost:5000 or http://127.0.0.1:5000

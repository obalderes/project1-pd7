from flask import Flask, request, render_template
import datastorage
import math
from flask import session,url_for,redirect,flash

global questions
#global email

questions = []
for line in open('question.txt').readlines():
   questions.append(line)





app = Flask(__name__)
app.secret_key = 'some_secret'

<<<<<<< HEAD
global questions
global email
global loggedin

q = open('question.txt')

@app.route("/",methods=['GET','POST'])
def home():
   if email in session:
      return redirect(url_for('/rate'))
=======
>>>>>>> f329fc9847b6407653d11420b48926b4b0cb2522

@app.route("/",methods=['GET','POST'])
def home():
   if session.get('username'):
      return redirect(url_for('rate'))
   else:
      return redirect(url_for('login'))
        
        

        
@app.route('/rate', methods=['GET','POST'])
def rate():
   
   if session.get('username'):
      #if request.method == 'POST':
      try:
         email
      except NameError:
         return redirect(url_for('logout'))

      info = datastorage.getData(email)

      projects = []
      count = 1
      while(count <= len(info)):
         projects.append(datastorage.getGroupMembers(email,str(count)))
         count = count + 1




      numratings = 0
      sumratings = 0
      scores = []
      for projs in info:
        for ratings in projs:
            numratings = numratings + 1
     #       sumratings = sumratings + info[projs][ratings]['score']
     #       scores.append(info[projs][ratings]['score'])
      avgrating = datastorage.getAvgOverallIndividualPoints(email)

      stdev = 0
      if numratings != 0:
         ex = 0
         for score in scores:
            ex = ex + (score-avgrating) * (score-avgrating)
         stdev = math.sqrt(ex/numratings)

      first = datastorage.getFirst(email)
      last = datastorage.getLast(email)



      questionavgs=[]
      
      for x in range(len(questions)):
         r=0
         for i in range(len(info)):
            r=r+datastorage.getTotalIndividualAvgForQuestion(email,x)#(email,i+1,questions[x])
            questionavgs.append(r/len(info))
      loggedin=True
         

         
      if request.method == 'POST':
         
         rater = email
         ratee = request.form('ratees')
         num = 0
         for n in questions:
            datastorage.ratePerson(rater=rater, ratee=ratee,question=n,score=request.form(n),comments=None)
     # rating1 = request.form('question1')
     # rating2 = request.form('question2')
     # rating3 = request.form('question3')
      
     # datastorage.ratePerson(rater=rater, ratee=ratee,question=questions[1],score=rating1,comments=None)
     # datastorage.ratePerson(rater=rater, ratee=ratee,question=questions[2],score=rating2,comments=None)

     # datastorage.ratePerson(rater=rater, ratee=ratee,question=questions[3],score=rating2,comments=None)
         

      return render_template('index.html',loggedin=True,projects=projects,questions=questions,avgrating=avgrating,stdev=stdev,questionavgs=questionavgs)

      #return render_template('index.html', loggedin=True)


<<<<<<< HEAD
 
=======


        
>>>>>>> f329fc9847b6407653d11420b48926b4b0cb2522
@app.route('/login', methods=['GET','POST'])
def login():
   if request.method == 'POST':
        ermail = request.form["username"]
        paswrd = request.form["idnum"]
        if datastorage.isUser(ermail):
           loggedin = True
           session["username"]=True
           global email
           email = ermail
        return redirect(url_for('home'))
   return render_template('index.html',loggedin=False,projects=None,questions=questions,avgrating=None,stdex=None,questionavgs=None)

@app.route('/logout')
def logout():
   session.pop('username', None)
   return redirect(url_for('home'))

<<<<<<< HEAD
=======

>>>>>>> f329fc9847b6407653d11420b48926b4b0cb2522
if __name__=="__main__":
    app.debug=True # remove this line to turn off debugging
    app.run(port=7007) # connect to localhost:5000 or http://127.0.0.1:5000

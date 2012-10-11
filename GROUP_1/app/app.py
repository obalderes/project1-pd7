from flask import Flask
from flask import session,url_for,request,redirect
import data

app = Flask(__name__)
app.secret_key="nothing"

#UserEmail=""
#logged_in = false

@app.route("/",methods=['GET','POST'])
def login():
	global logged_in = false
	global UserEmail = ""
	UserCode = ""
	error = None
	if request.method == 'POST':
		UserEmail = request.form["user"]
        	UserCode = request.form["idnum"]
		if data.checkLogin (UserEmail, UserCode):
			logged_in = true
			return redirect(url_for('home'))
		else:
			error =  "Member name and password were not found. Please try again."   
	return render_template("login.html", error = error)
#logging in by comparng the username and idnumber, if the input is incorrect the login fails and the user gets an error message

@app.route("/home", methods = ['GET', 'POST'])
def home():
	global UserEmail
	global logged_in
	RatedEmail =""
	error = None
	if logged_in = true:
		A1=data.getRatingof(UserEmail) 
		A2=data.getRatingof(UserEmail) 
		A3=data.getRatingof(UserEmail) 
		A4=data.getRatingof(UserEmail) 
#The "A"s are the answers to each question
#This whole part still need the function to know how the data will return
		if request.method == 'POST':  
			button = request.form['button']
        		if button == 'logout':
				logged_in = false
    				return redirect(url_for('login'))
			else:
				RatedEmail = request.form["user"]
				if data.getGroupNo(RatedEmail) == data.getGroupNo(UserEmail):
					data.setratings(UserEmail, RatedEmail,request.form["select1"],request.form["select2"],request.form["select3"],request.form["select4"])
					return redirect(url_for('home'))
		#using set rating and then redirecting the user home
	else:
		return redirect(url_for('login'))
#if someone jsut types /home at the end of the url without logging in they will just go back to the login page	
	return render_template("home.html", error = error,A1=A1,A2=A2,A3=A3,A4=A4)			

if __name__ == "__main__":
    app.debug=True
    app.run()

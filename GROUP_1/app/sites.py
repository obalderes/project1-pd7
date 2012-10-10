from flask import Flask
from flask import session,url_for,request,redirect

app = Flask(__name__)
app.secret_key=""

@app.route("/")
def index():
����if 'user' in session:
��������return redirect(url_for('home'))
����else:
��������return redirect(url_for('login'))

����
@app.route("/home", methods = ['GET', 'POST'])
def home():
	if request.method == 'GET':��
		if 'user' in session:
���������		return render_template("home.html")
#Allen & Olivia:if you need another page for viewing pages i'll add it, but with tabs one should work
#that being said i want to make a different post ratings page later,but for now i'm good with this
	else:
��������return redirect(url_for('login'))
button = request.home["button"]
��������if button == "logout":
		session.pop('user',None)
����		return redirect(url_for('login'))�
	   if button == "post ratings":
		return redirect(url_for('rating'))

@app.route("/post_ratings",methods=['GET','POST'])
def rating():	
	if request.method == 'GET':
		return render_template("ratings.html")
	if request.method == "POST":
		#post
#depending on the template we can change this
	return render_template("rating.html")
	
@app.route("/login",methods=['GET','POST'])
def login():
����if request.method == 'POST':
��������session['user'] = request.form['user']
��������return redirect(url_for('home'))
����return
	 '''
        	<form action="" method="post">
        	  	  <p><input type=text name=user>
           	 <p><input type=submit value=Login>
  	    	  </form>
    	'''
#we can use this login method until we get a login template
#ill add a way to reject users soon aswell


if __name__ == "__main__":
����app.debug=True
����app.run()
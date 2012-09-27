from flask import Flask
from flask import  url_for, redirect, flask, request
from flask import render_template

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
	if request.method == "GET":
		return render_template("form.html")
	else:
		button = request.form['button']
		name = request.form['username']
		assert name != ""
		flash("Name: %s" % (name))
		return redirect(url_for('home/' + name)
	#return "This is David's really cool test page. It's in the works."
	#return url_for('hello')
	#return redirect(url_for('hello'))

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name = None):
	return render_template("hello.html", name = name)

if __name__ == "__main__":
	app.debug = True
	app.run()

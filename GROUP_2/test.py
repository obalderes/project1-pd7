from flask import Flask
from flask import url_for, redirect, request, flash
from flask import render_template

app = Flask(__name__)
app.secret_key = "Group 2 rules!"

@app.route("/", methods = ['GET', 'POST'])
def home():
	if request.method == "GET":
		return render_template("form.html")
	else:
		button = request.form['button']
		username = request.form['username']
		assert username != ""
		flash("Name: " + username)
		return redirect(url_for('hello', name = username))
	#return "This is David's really cool test page. It's in the works."
	#return url_for('hello')
	#return redirect(url_for('hello'))

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name = None):
	return render_template("hello.html", name = name)

def view_results():
    if request.method == "GET":
        return render_template("results.html")
    else:
        button = request.form['button']
    	username = request.form['username']
	assert username != ""
	flash("Name: " + username)
	return redirect(url_for('results', name = username))

@app.route("/results")
def results(name = None):
	return render_template("results.html", name = name)


if __name__ == "__main__":
	app.debug = True
	app.run()

from flask import Flask, url_for
from flask import render_template
app = Flask(__name__)

@app.route("/")
def home():
	return "This is David's really cool test page. It's in the works."

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name = None):
	return render_template("hello.html", name = name)

if __name__ == "__main__":
	app.debug = True
	app.run()

from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
	return "This is David's really cool test page. It's in the works."

if __name__ == "__main__":
	app.debug = true
	app.run()

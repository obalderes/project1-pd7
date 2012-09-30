import time
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def print_page():
    return render_template("index.html")

@app.route("/rate")
def rate_page():
    return render_template("rate.html")

if __name__ == "__main__":
    app.run(debug=True)


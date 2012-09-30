import time
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def print_page():
    return render_template("index.html")

@app.route("/login")
def login_page():
    text = "Login page"
    return text

if __name__ == "__main__":
    app.run(debug=True)


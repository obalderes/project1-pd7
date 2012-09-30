import time
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def print_page():
    text = "<b>Ratebook<b>"
    text 
    return text

@app.route("/login")
def login_page():
    text = "Login page"
    return text

if __name__ == "__main__":
    app.run(debug=True)


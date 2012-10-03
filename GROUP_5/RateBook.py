from flask import Flask
from flask import url_for, redirect, request, render_template

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def index_page():
    if request.method=="GET":
        return render_template("index.html")
    elif request.method=="POST":
        button = request.form['button']
        email = request.form['email']
        assert email != ""
        return redirect(url_for("rate", name = email))


@app.route("/rate")
@app.route("/rate/<name>", methods = ['GET', 'POST'])
def rate(name = "Stranger"):
    return render_template("rate.html", name = name)

if __name__ == "__main__":
    app.run(debug=True)

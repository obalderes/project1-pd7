from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    name="Thluffy"
    return render_template("page.html", name=name)


if __name__ == "__main__":
    app.run(debug=True)


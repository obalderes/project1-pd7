from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/testtemp")
def testtemp():
    name = "Bob"
    return render_template('testtemp.html',name = name)

if __name__ == "__main__":
    app.debug = True
    app.run()


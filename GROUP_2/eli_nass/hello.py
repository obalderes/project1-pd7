from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    
    if request.method == "GET":
        return render_template("t1.html")
    else:
        return render_template("t2.html")


if __name__ == '__main__':
    app.run(debug=True)

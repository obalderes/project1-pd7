from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    info="This text is brought to you from the python file."
    return render_template('index.html',info=info)

if __name__ == "__main__":
    app.run(debug=True)

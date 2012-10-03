import Flask
import database

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/", methods = ['GET', 'POST'])
